from flask import Flask, jsonify
import random

from openai import OpenAI

app = Flask(__name__)

compliments = [
    "You're amazing!",
    "You have a great smile!",
    "You're a true inspiration!",
    "Your kindness knows no bounds!",
    "You're exceptionally talented!",
]

insults = [
    "You're not the brightest bulb in the box.",
    "You couldn't pour water out of a boot with instructions on the heel.",
    "I've seen smarter people at a zoo.",
    "You're as useful as a screen door on a submarine.",
    "You're a walking advertisement for the benefits of birth control.",
]

#Using second person perspective, give me a one liner roast  for a comedy script using following keywords: "bald", "mustache" 

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/compliment', methods=['GET'])
def get_compliment():
    return jsonify({"compliment": random.choice(compliments)})

@app.route('/insult', methods=['GET'])
def get_insult():
    return jsonify({"insult": random.choice(insults)})


