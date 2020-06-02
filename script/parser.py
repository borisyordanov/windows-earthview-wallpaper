import urllib.request
import json
from bs4 import BeautifulSoup
result = []
file = open('output.txt','a')
for x in range(1000, 1005 ): #You should able to run this in parallel, but I don't know how to do it
	x = str(x)
	try:
		print("Fetching" + x + " ...")
		response = urllib.request.urlopen('https://earthview.withgoogle.com/' + x)
		html = response.read()
		html = BeautifulSoup(html)
		Region = str((html.find("div", class_="content__location__region")).text.encode('utf-8'))
		Country = str((html.find("div", class_="content__location__country")).text.encode('utf-8'))
		Everything = html.find("a", id="globe", href=True)
		GMapsURL = Everything['href']
		Image = 'https://www.gstatic.com/prettyearth/assets/full/' + x + '.jpg'
		result.append({'region': Region, 'country': Country, 'map': GMapsURL, 'image': Image})
	
	except:
		continue #If the page is 404, then it will skip to the next one

meow = json.dumps(result) #because I love cat...
file.write(meow)			
file.close()
