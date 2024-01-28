import pickle


MODEL_PATH = ''


class FacialFeaturesModel:
    def __init__(self):
        with open(MODEL_PATH, 'rb') as fp:
            self.model = pickle.load(fp)

    def predict(self, x):
        return self.model.predict(x)
