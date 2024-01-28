import pickle
import numpy as np

from CommentGenerator.creating_facial_features_model.global_variables import PATH_TO_IMAGES
from CommentGenerator.creating_facial_features_model.preprocess import file_name_to_img

with open('model.txt', 'rb') as fp:
    model = pickle.load(fp)

img = file_name_to_img(PATH_TO_IMAGES + '{:06d}'.format(190000) + '.jpg')
print(img)
print(img.shape)
print(model.predict(np.array([img])))
