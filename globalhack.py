from flask import Flask, request, render_template
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return render_template('index.html')



