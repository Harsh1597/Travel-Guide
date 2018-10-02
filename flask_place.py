from flask import Flask
import requests
from bs4 import BeautifulSoup
import json




app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

@app.route('/<place_name>')
def place(place_name):
	token = []
	url = 'https://www.holidify.com/places/' + place_name +'/sightseeing-and-things-to-do.html'
	request = requests.get(url)
	soup = BeautifulSoup(request.text,"html.parser")
	data = soup.find_all('h2',{"class":"ptvObjective"})
	for each in data:
		store = each.text
		token.append(store);
	return json.dumps(token)

if __name__ == '__main__':
    app.run(debug=True)
