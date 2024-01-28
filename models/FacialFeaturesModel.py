from keras.models import load_model


MODEL_PATH = ''


class FacialFeaturesModel:
    def __init__(self):
        self.model = load_model('model.keras')

    def predict(self, x):
        return self.model.predict(x)
