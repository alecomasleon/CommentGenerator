from flask import Flask, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": 'Hello, World!'})

keywords="cuban, mustache, blonde"

@app.route('/compliment', methods=['GET'])
def get_compliment():
    return jsonify({"compliment": get_compliment(keywords)})

@app.route('/roast', methods=['GET'])
def get_insult():
    return jsonify({"roast": get_roast(keywords)})

#open AI 
from openai import OpenAI

client = OpenAI(api_key='INSERTKEY')

def get_roast(keywords):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional standup comedian " +
            "Your job is to come up with a one liner roast based on the given keywords "+ 
            "based on the given keywords that represents the customer's apperance."},
            {"role": "user", "content": 
             "Give me a one liner roast using these comments:" + keywords}
        ]
    )
    return response.choices[0].message.content


def get_compliment(keywords):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional Customer Service Representatives " +
            "Your job is to come up with a one liner compliment to the customer" +
            "based on the given keywords that represents the customer's apperance."},
            {"role": "user", "content": 
             "Give me a one liner compliment using these comments:" + keywords}
        ]
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True, port=9000)

