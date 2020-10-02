import requests
from bs4 import BeautifulSoup as bs

#load the webpage content
writers = [
    "https://en.wikipedia.org/wiki/J._R._R._Tolkien",
    "https://en.wikipedia.org/wiki/Dan_Simmons",
    "https://en.wikipedia.org/wiki/George_Orwell",
    "https://en.wikipedia.org/wiki/Stephen_King",
    "https://en.wikipedia.org/wiki/William_Shakespeare",
    "https://en.wikipedia.org/wiki/George_R._R._Martin",
    ]

talalatok = []

for i in range(len(writers)):    
    print(writers[i]) 
    r = requests.get(writers[i])
    #convert to bs object
    soup = bs(r.content)
    print(soup.prettify())
    try:
        try:
            writer = soup.find('h1', class_='firstHeading', id='firstHeading').text
        except:
            writer = "nem talált író!"
        try:
            shortDesc = soup.find('div', class_='shortdescription nomobile noexcerpt noprint searchaux').text
        except:
            shortDesc = "nem talált short description"
        try:
            bday = soup.find('span', class_='bday').text
        except: 
            bday = "nem talált birthday"
        print(writer + " (" + bday + "): " + shortDesc)
        talalatok.append(writer + " (" + bday + "): " + shortDesc)
    except:
        print("nem talált semmit!")
        talalatok.append("nem talált text")

with open('C:/IT Workshop/BeautifulSoup/writers.txt', 'w') as filehandle:
    for listitem in talalatok:
        filehandle.write('%s\n' % listitem)