import secrets
from flask import Flask, render_template
import requests


key = secrets.api_key
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome!<h1>' 

@app.route('/name/<name>')
def hello_name(name):
    return render_template('name.html', name=name)

@app.route('/headlines/<name>')
def find_titles(name):
    request_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
    user_key = {"api-key": key}
    response = requests.get(request_url, user_key).json()
    article_title = []
    link_list = []
    for item in response["results"]:
        article_title.append(item["title"])
        link_list.append(item["url"])
    return render_template('headline.html',name=name, list=article_title, url_list=link_list)   

@app.route('/images/<name>')
def find_titles_with_image(name):
    request_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
    user_key = {"api-key": key}
    response = requests.get(request_url, user_key).json()
    article_title = []
    link_list = []
    picture_list=[]
    for item in response["results"]:
        article_title.append(item["title"])
        link_list.append(item["url"])
        picture_list.append(item["multimedia"][0]["url"])
    return render_template('extra_credit.html',name=name, list=article_title, url_list=link_list, image_list=picture_list)  

if __name__ == '__main__':  
    app.run()
