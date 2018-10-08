# Importing required packages
from flask import Flask # Python web framework
import requests # To make request to the url 
from bs4 import BeautifulSoup # Web scrapping tool
import json # To convert dict to json and json to dict

# Creating falsk app
app = Flask(__name__)

# Routes
@app.route('/')
def hello_world():
  message = { "message": "App is working" }
  message = json.dumps(message) # Creating a json object
  return message 

# /<place>
@app.route('/<place>')
def thingsTodo(place):
	placesToVisit = {} # 
	url = 'https://www.holidify.com/places/' + place +'/sightseeing-and-things-to-do.html'
	request = requests.get(url)
  # Making a soup for scrapping
	soup = BeautifulSoup(request.text, "html.parser")
	places = soup.find_all('h2',{ "class":"ptvObjective" })
	for eachPlace in places:
		eachPlace = eachPlace.text
		eachPlace = eachPlace.split('. ') 
		placesToVisit[eachPlace[0]]= eachPlace[1] # Append place to dict 
	placesToVisit = json.dumps(placesToVisit) # converting dict to json
	return placesToVisit

if __name__ == '__main__':
    app.run(debug=True)
