from flask import Flask, request
from random import choice, randint


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def index():
    """Home page."""

    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    """Say hello"""

    return "<html><body><h1>Hello!</h1></body></html>" #add code here to greet user

@app.route('/lucky')
def lucky_number():
    """Provides a random lucky number"""
    # add code here of getting a lucky number and return a string
    # with the lucky number
    lucky_num = randint(1,100)
    lucky_message = "Your lucky number is %s" % lucky_num
    return "<html><body><h1> %s </h1></body></html>" % lucky_message

@app.route('/kitten')
def kittens():
    height = raw_input("Enter a height!")
    width = raw_input("Enter a width!")
    return '<img src="http://placebeard.it/%s/%s"/>' % (height,width)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
