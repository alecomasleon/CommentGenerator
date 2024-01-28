from fer import FER


class EmotionDetector:
    def __init__(self):
        self.detector = FER()

    def get_most_prominent_emotion(self, img):
        result = self.detector.detect_emotions(img)

        print(result)
        return max(result[0]['emotions'], key=lambda x: result[0]['emotions'][x])
