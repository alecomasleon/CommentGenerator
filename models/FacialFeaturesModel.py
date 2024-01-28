from keras.models import load_model
import numpy as np


MODEL_PATH = '/Users/alejandro/PycharmProjects/CommentGenerator/CommentGenerator/models/model.keras'


class FacialFeaturesModel:
    def __init__(self):
        self.model = load_model(MODEL_PATH)

    def predict(self, img):
        return self.model.predict(np.array([img]))[0]
