import responses
import requests
import flask
import json
import os
from flask import request, jsonify, abort, Flask, render_template, redirect, url_for, session

app = Flask(__name__)

list_url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations'
id_url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/1'
name_url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/{name}'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login2.html')
    else:
        return "Welcome to the Age Of Empires II!"

@app.route('/list', methods=['GET'])
def api_all():
    response = requests.get(list_url).json()
    dictx = {'name': [], 'army_type': []}

    for x in response.values():
        new_response  = x
        for i in x:
            dictx['name'].append(i['name'])
            dictx['army_type'].append(i['army_type'])
    #return jsonify(dictx)
    return render_template('result.html', result = new_response)

@app.route('/list/<thename>', methods=['GET'])
def the_name(thename):
    url = name_url.format(name = thename)
    response2 = requests.get(url)
    if response2.status_code == 200:
        jsondata =response2.json()
        the_name = {'ID': jsondata['id'], 'thename': jsondata['name'], 'army_type': jsondata['army_type']}
        #return jsonify(jsondata)
        return render_template('result2.html', result2 = jsondata)
    else:
        return "Error! Name not found", 404

if __name__ == "__main__":
    app.run(port=8000, debug=True)
