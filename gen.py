#!usr/bin/python3

import re
import urllib
import time
import random
import bs4 as bs
import os
from django.template import loader


query = raw_input("Please enter your desired query: ")

imageSites = ['https://yandex.com/images/search?text='+query, 'http://www.bing.com/images/search?q='+query, 'https://duckduckgo.com/?q='+query+'&t=he&iax=1&ia=images', 'https://images.search.yahoo.com/search/images;_ylt=AwrBTzxaycpYj8YAimhXNyoA;_ylu=X3oDMTE0bG41bTRiBGNvbG8DYmYxBHBvcwMxBHZ0aWQDQjM2MjZfMQRzZWMDcGl2cw--?p='+query+'&fr2=piv-web&fr=yfp-t', 'http://www.gettyimages.com/photos/hackers?excludenudity=true&mediatype=photography&page=1&phrase='+query+'&sort=mostpopular']
textSites = ['https://en.wikipedia.org/wiki/'+query, 'www.thefreedictionary.com/'+query]
storedImages = []
storedText = []

def imageScraper():

#random website is generated form 'siteList' variable
	check = random.randint(0,3)
	if check == 0:
		site  = urllib.urlopen(imageSites[0])
		print("Pulling from Yandex database....please wait.")
		time.sleep(1)
		html = site.read()
		soup = bs.BeautifulSoup(html, 'lxml')
		for line in (soup.find_all('img')):
			links = (line.get('src'))
			storedImages.append(links)

	elif check == 1:
		site2 = urllib.urlopen(imageSites[1])
		print("Pulling from Bing database...please wait.")
		time.sleep(1)
		html2 = site2.read()
		soup2 = bs.BeautifulSoup(html2, 'lxml')
		for line in (soup2.find_all('img')):
			links = (line.get('src'))
			storedImages.append(links)

	elif check == 2:
		site3 = urllib.urlopen(imageSites[2])
		print("Pulling from Yahoo Images database....please wait.")
                time.sleep(1)
		html3 = site3.read()
                soup3 = bs.BeautifulSoup(html3, 'lxml')
                for line in (soup3.find_all('img')):
                        links = line.get('src')
			storedImages.append(links)

	elif check == 3:
		site4 = urllib.urlopen(imageSites[3])
		print("Pulling from Getty Images....please wait.")
		time.sleep(1)
		html4 = site4.read()
		soup4 = bs.BeautifulSoup(html4, 'lxml')
		for line in (soup4.find_all('img')):
			links = line.get('src')
			storedImages.append(links)


	for image in storedImages:
		name = random.randrange(1, 1000)
		urllib.request.urlretrieve(image, name)

	print(str(len(storedImages))+'were successfully downloaded....')






#def textScraper():

#def Template()
	#template = loader.get_template(/) #make sure to create another list with all of the paths in it for random selection of templates.

def Main():

	imageScraper()

	'''textScraper()

	Template()


	#Templater()'''


#run main function
if __name__ == '__main__':
	Main()

#sites will be in a seperate list.
#parse images tags form sites using urllib
#loop through a list in order to find a sites to pull from
#make script randomly generate a number and use that number as a reference for which tag (from which site) to use.
#give user additional information
#***https://images.google.com/ --for images***
#Django will look in the templates folder (that you created) by default in order to search a template. Including "template" in the path of loader.get_template(PATH) is not necessary.
#Create Template in variable and pipe into an HTML file using the os module.
#for-loops may need to be unnested.
#additional templates can be found at: http://www.free-css.com/free-css-templates
