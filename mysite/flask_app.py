from flask import Flask, render_template, request, redirect, url_for
import time
from random import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("MainPage.html")
