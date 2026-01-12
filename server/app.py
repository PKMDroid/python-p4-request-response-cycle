#!/usr/bin/env python3

import os
from flask import Flask, request, current_app, g, make_response, redirect, abort

app = Flask(__name__)

@app.before_request
def set_app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    return make_response(response_body, 200, {})

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

@app.route('/reginald-kenneth-dwight')
def redirect_example():
    return redirect('https://names.com/elton-john')

@app.route('/check/<string:name>')
def abort_example(name):
    if name != "valid":
        abort(404)
    return f'<h1>{name} is valid!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
