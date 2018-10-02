import requests
from bs4 import BeautifulSoup
import json

# url = 'https://www.holidify.com/places/nasik/sightseeing-and-things-to-do.html'

query = raw_input("Enter Place Name: ")
url = 'https://www.holidify.com/places/' + query +'/sightseeing-and-things-to-do.html'
request = requests.get(url)
soup = BeautifulSoup(request.text,"html.parser")
data = soup.find_all('h2',{"class":"ptvObjective"})
for each in data:
	print each.text
