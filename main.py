from flask import Flask, jsonify
import os
from openai import OpenAI
import random
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": 'Hello, World!'})

keywords="big eye, mustache, blonde"

@app.route('/compliment', methods=['GET'])
def get_compliment():
    return jsonify({"compliment": get_compliment(keywords)})

@app.route('/roast', methods=['GET'])
def get_insult():
    return jsonify({"roast": get_roast(keywords)})

# open AI 
client = OpenAI(api_key= os.environ.get("OPENAI_API_KEY"))
# def make_rand(keywords):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a professional standup comedian " +
#             "Your job is to come up with a similar words based on the given keywords "+ 
#             "based on the given keywords that represents the customer's apperance."},
#             {"role": "user", "content": 
#              "Give me 3 similar keywords of each of these keyword, dont label them by numbers:" + keywords}
#         ]
#     )
#     str_data=response.choices[0].message.content
#     # words = str_data.replace('\n', ' ').replace('.',' ').replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ').replace('roast','').replace(':','').replace('"',' ').replace("'",' ').replace("  ", " ").replace("  ", " ").split()

#     # array = [words[i:i+4] for i in range(0, len(words), 4)]
#     # random_words_list = []

#     # for row in array:
#     #     random_word = random.choice(row)
#     #     random_words_list.append(random_word)

#     # strin=' '.join(random_words_list)
#     print (str_data)
#     return str_data

def get_roast(keywords):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional standup comedian " +
            "Your job is to come up with a two line roast based on the given keywords "+ 
            "based on the given keywords that represents the customer's apperance."},
            {"role": "user", "content": 
             "Give me a two line roast using these comments:" + keywords}
        ]
    )
    return response.choices[0].message.content

def get_compliment(keywords):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional Customer Service Representatives " +
            "Your job is to come up with a two line compliment to the customer" +
            "based on the given keywords that represents the customer's apperance."},
            {"role": "user", "content": 
             "Give me a two line compliment using these comments:" + keywords}
        ]
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True, port=9000)