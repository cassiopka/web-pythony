from flask import Flask, render_template, request

app = Flask(__name__)

application = app

@app.route('/')
def index():
    msg = 'Hello world'
    return render_template('index.html',msg=msg)

