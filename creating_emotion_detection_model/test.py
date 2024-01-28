from fer import FER
import cv2 as cv

from CommentGenerator.creating_emotion_detection_model.EmotionDetector import EmotionDetector

PATH_TO_ALL_DATA = '../../data/'
PATH_TO_IMAGES = PATH_TO_ALL_DATA + 'img_align_celeba/'

img_str = '000047.jpg'
img = cv.imread(PATH_TO_IMAGES + img_str)
# img = cv.resize(img)
print(img)
print(type(img))
print(img.shape)

detector = EmotionDetector()
print(detector.get_most_prominent_emotion(img))

cv.imshow("Display window", img)

k = cv.waitKey(0)
cv.destroyAllWindows()
