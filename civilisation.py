import responses
import requests
import flask
import json
from flask import request, jsonify, abort, Flask, render_template, redirect, url_for

app = Flask(__name__)

list_url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations'
id_url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/1'
name_url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/{name}'

#this allows the external link to load a login page before any data could be accessed
@app.route('/', methods=['GET', 'POST'])
def hello():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('homepage.html')
    return render_template('login2.html', error=error)

#this section is to be able to see all the lists of civilizations within the game
@app.route('/list', methods=['GET'])
def api_all():
    response = requests.get(list_url).json()
    dictx = {'name': [], 'army_type': []} #this will list the name of the civilisations as well as the type of army that they belong to.

    for x in response.values():
        new_response  = x
        for i in x:
            dictx['name'].append(i['name']) #there are two for loops as the information displayed is within civilisations
            dictx['army_type'].append(i['army_type'])
    #return jsonify(dictx)
    return render_template('result.html', result = new_response)

@app.route('/list/<thename>', methods=['GET'])
def the_name(thename):
    url = name_url.format(name = thename)
    response2 = requests.get(url)
    if response2.status_code == 200:
        jsondata =response2.json()
        the_name = {'ID': jsondata['id'], 'thename': jsondata['name'], 'army_type': jsondata['army_type']} #this will list the name of the civilisations as well as the type of army that they belong to and the ID number of the team
        #return jsonify(jsondata)
        return render_template('result2.html', result2 = jsondata)
    else:
        return "Error! Name not found", 404 #this error code will be displayed if the name of the civilsation does not exist in the data

if __name__=="__main__":
    app.run(port=8000, debug=True)
