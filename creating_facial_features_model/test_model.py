import pickle
import pandas as pd
import keras
import numpy as np
import cv2 as cv
from keras import optimizers, Sequential, layers

from CommentGenerator.creating_facial_features_model.BatchGenerator import BatchGenerator
from CommentGenerator.creating_facial_features_model.global_variables import PATH_TO_IMAGES, START_VAL, START_TEST, \
    NUM_IMAGES, PATH_TO_ALL_DATA
from CommentGenerator.creating_facial_features_model.preprocess import file_name_to_img

# with open('modelMSE.txt', 'rb') as fp:
    # model = pickle.load(fp)

model = keras.models.load_model('modelPSN.keras')

headers_str = '5_o_Clock_Shadow,Arched_Eyebrows,Attractive,Bags_Under_Eyes,Bald,Bangs,Big_Lips,Big_Nose,Black_Hair,Blond_Hair,Blurry,Brown_Hair,Bushy_Eyebrows,Chubby,Double_Chin,Eyeglasses,Goatee,Gray_Hair,Heavy_Makeup,High_Cheekbones,Male,Mouth_Slightly_Open,Mustache,Narrow_Eyes,No_Beard,Oval_Face,Pale_Skin,Pointy_Nose,Receding_Hairline,Rosy_Cheeks,Sideburns,Smiling,Straight_Hair,Wavy_Hair,Wearing_Earrings,Wearing_Hat,Wearing_Lipstick,Wearing_Necklace,Wearing_Necktie,Young'
headers = headers_str.split(',')


def formal_tests():
    batch_size = 40
    x_test_filenames = list(PATH_TO_IMAGES + '{:06d}'.format(i + 1) + '.jpg' for i in range(START_TEST, NUM_IMAGES))
    y_test = pd.read_csv(PATH_TO_ALL_DATA + 'list_attr_celeba.csv')
    y_test = y_test.drop('filename', axis=1)

    my_testing_batch_generator = BatchGenerator(x_test_filenames, y_test[START_TEST:NUM_IMAGES], batch_size)

    result = model.evaluate(my_testing_batch_generator)
    print(result)


def predict_to_dict(preds):
    dic = {}
    print(len(preds[0]))
    print(len(headers))
    for i in range(len(preds[0])):
        dic[headers[i]] = preds[0][i]

    return dic


def test():
    img = file_name_to_img(PATH_TO_IMAGES + '{:06d}'.format(182839) + '.jpg')
    preds = model.predict(np.array([img]))
    print(preds)
    print(predict_to_dict(preds))

    cv.imshow("Display window", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def test_subjects():
    img = file_name_to_img('../../test_subjects/' + 'danny2' + '.JPG')
    preds = model.predict(np.array([img]))
    print(preds)
    print(predict_to_dict(preds))

    cv.imshow("Display window", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# formal_tests()
test_subjects()
