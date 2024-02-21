from aifc import Error

from flask import Flask, jsonify, request, Response
import os
from openai import OpenAI
import random
from dotenv import load_dotenv
import cv2 as cv
import time
from flask_cors import CORS, cross_origin

from models.EmotionDetector import EmotionDetector
from models.FacialFeaturesModel import FacialFeaturesModel
from key_words import get_emotion, get_attributes, gen_keys

emotionDetector = EmotionDetector()
facialFeaturesModel = FacialFeaturesModel()
load_dotenv()

app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'application/json'

@app.route('/')
def hello_world():
    return jsonify({"message": 'Hello, World!'})

@app.route('/compliment', methods=['GET'])
def get_compliment():
    return jsonify({"compliment": get_compliment(keywords)})

@app.route('/roast', methods=['GET'])
def get_insult():
    return jsonify({"roast": get_roast(keywords)})


DOWNLOADS_PATH = "/Users/alejandro/Downloads/"
FILE = "/Users/alejandro/Downloads/INC_MSG.txt"

@app.route('/temp', methods=["GET", "POST"])
def temp():
    response = jsonify({'msg': "hiiii"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add("Access-Control-Allow-Headers", "*")
    # response.headers.add("Access-Control-Allow-Methods", "*")
    return response

@app.route('/request', methods=["GET", "POST"])
def receive_image():
    name = request.args.get('name')
    print(name)

    # img = ''
    # for i in range(3):
    #     try:
    #         img = cv.imread(DOWNLOADS_PATH + name)
    #     except:
    #         print("imread failed")
    #         time.sleep(200)
    #
    # if img is None:
    #     raise Error("imread failed 3 times")

    time.sleep(0.5)
    img = cv.imread(DOWNLOADS_PATH + name)
    img = cv.resize(img, (256, 256))
    ff = facialFeaturesModel.predict(img).tolist()
    print(img)
    print(ff)
    # emotion = emotionDetector.get_most_prominent_emotion(img)

    # keys = gen_keys(ff, emotion)
    keys = gen_keys(ff)

    if random.random() < 0.75:
        msg = get_roast(keys)
    else:
        msg = get_compliment(keys)

    print(msg)
    with open(FILE, 'w') as f:
        f.write(msg)

    response = jsonify({'msg': msg})
    response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add("Access-Control-Allow-Headers", "*")
    # response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route('/process', methods=['GET', 'POST'])
def get_message(uuid):
    #content = request.args.get('url')
    return jsonify({"roast": get_roast(keywords)})

#open AI 
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
            "Your job is to come up with a two liner roast based on the given keywords "+ 
            "based on the given keywords that represents the customer's apperance."},
            {"role": "user", "content": 
             "Give me a two liner roast using these comments:" + keywords}
        ]
    )
    return response.choices[0].message.content


def get_compliment(keywords):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional Customer Service Representatives " +
            "Your job is to come up with a two liner compliment to the customer" +
            "based on the given keywords that represents the customer's apperance."},
            {"role": "user", "content": 
             "Give me a two liner compliment using these comments:" + keywords}
        ]
    )
    return response.choices[0].message.content


if __name__ == '__main__':
    app.run(debug=True, port=9000)
