'''
##############################################
File: app.py
Project: hello_flask
Desc: 
File Created: Friday, 18th November 2022 2:06:24 pm
Author: Leoncio López (leobip27@gmail.com)
-----
Last Modified: Friday, 18th November 2022 2:06:48 pm
Modified By: Leoncio López (leobip27@gmail.com>)
-----
Copyright <<projectCreationYear>> - 2022 Your Company, Your Company
################################################
'''


from flask import Flask, jsonify, request

app = Flask(__name__)

# Home
@app.route("/")
def index():
    return "<h1>HELLO WORLD! </h1>"

# Para pasar un parametro a usar en la pagina en la url, cun valor default
@app.route("/home", defaults={'name':''})
@app.route("/home/<name>")
def home(name):
    return "<h1>Hello {} from Flask!, you  are on the home page.</h1>".format(name)


@app.route('/json')
def json():
    return jsonify({'Nombre': 'json2', 'key2':[1,2,3]})

# Otra forma de obtener input
# ex: http://127.0.0.1:5000/query?name=Leo&location=Venezuela
# ex: http://127.0.0.1:5000/query?name=Leo&location=Punto Fijo - Venezuela
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}, You are on the query page.!</h1>'.format(name, location)


# Uso de un formulario
@app.route('/theform')
def theform():
    return '''<form method = "POST" action = "/process">
                <input type = "text" name = "name">
                <input type = "text" name = "location">
                <input type = "submit" value = "Submit">
            </form>'''

@app.route('/process', methods = ['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    
    return '<h1>Hello {}. You are from {}, You submit your form succesfully!</h1>'.format(name, location)


if __name__ == '__main__':
    app.run(host='0.0.0.0')



