from flask import Flask, render_template

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''

@app.route('/')
def home():
    return 'My home page'

@app.route('/about')
def about():
    return render_template('about.html')
