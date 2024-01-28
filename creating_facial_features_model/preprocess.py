import pickle
from CommentGenerator.creating_facial_features_model.global_variables import PATH_TO_ALL_DATA, NUM_IMAGES, \
    PATH_TO_IMAGES, IMAGE_SIZE
import pandas as pd
import cv2 as cv
import pickle
import keras
import tensorflow as tf
import cv2 as cv
import pandas as pd

from CommentGenerator.creating_facial_features_model.global_variables import PATH_TO_ALL_DATA, NUM_IMAGES, \
    PATH_TO_IMAGES, IMAGE_SIZE


def convert_attr_to_csv():
    input_file_path = PATH_TO_ALL_DATA + 'list_attr_celeba.txt'
    output_file_path = PATH_TO_ALL_DATA + 'list_attr_celeba.csv'

    # Read the tab-separated text file, skipping the first line
    txtf = open(input_file_path, 'r')
    csvf = open(output_file_path, 'w')

    first = True
    final = 'filename,'
    for line in txtf.readlines():
        if first:
            first = False
            continue

        final += line.replace(' ', ',').replace(',,', ',').replace(',,,', ',').replace('Young,', 'Young').replace('-1',
                                                                                                                  '0')

    csvf.write(final)
    txtf.close()
    csvf.close()
    print(f'Conversion completed. CSV file saved at: {output_file_path}')


def convert_part_to_csv():
    input_file_path = PATH_TO_ALL_DATA + 'list_eval_partition.txt'
    output_file_path = PATH_TO_ALL_DATA + 'list_eval_partition.csv'

    # Read the tab-separated text file, skipping the first line
    txtf = open(input_file_path, 'r')
    csvf = open(output_file_path, 'w')

    first = True
    final = 'name,section\n'
    for line in txtf.readlines():
        if first:
            first = False
            continue

        final += line.replace(' ', ',').replace(',,', ',').replace(',,,', ',')

    csvf.write(final)
    txtf.close()
    csvf.close()
    print(f'Conversion completed. CSV file saved at: {output_file_path}')


def create_x():
    train = []
    test = []
    for i in range(1, 162769):
        img_str = '{:06d}'.format(i) + '.jpg'
        print(img_str)
        img = cv.imread(PATH_TO_IMAGES + img_str)
        img = cv.resize(img, IMAGE_SIZE)

        train.append(img)

    with open(PATH_TO_ALL_DATA + 'x_train', 'wb') as fp:
        pickle.dump(train, fp)

    train = []

    for i in range(162769, NUM_IMAGES + 1):
        img_str = '{:06d}'.format(i) + '.jpg'
        print(img_str)
        img = cv.imread(PATH_TO_IMAGES + img_str)
        img = cv.resize(img, IMAGE_SIZE)

        test.append(img)

    with open(PATH_TO_ALL_DATA + 'x_test', 'wb') as fp:
        pickle.dump(test, fp)


def create_y():
    attr = pd.read_csv(PATH_TO_ALL_DATA + 'list_attr_celeba.csv')


def file_name_to_img(file_name):
    # print(file_name)
    img = cv.imread(file_name)
    img = cv.resize(img, IMAGE_SIZE)
    return img


def train():
    train_x = keras.utils.image_dataset_from_directory(PATH_TO_IMAGES, validation_split=0.2, subset="training",
                                                       seed=123, image_size=(256, 256), batch_size=50)
    print(train_x)
    for image_batch, labels_batch in train_x:
        print(image_batch.shape)
        print(labels_batch.shape)
        break


df = pd.read_csv(PATH_TO_ALL_DATA + 'list_eval_partition.csv')
for ind in df.index:
    if df['section'][ind] == 2:
        print(ind)
        break

# convert_attr_to_csv()

# pf = pd.read_csv(PATH_TO_ALL_DATA + 'list_attr_celeba.csv')
# print(pf.head())

# file_names = list(file_name_to_img(PATH_TO_IMAGES + '{:06d}'.format(i) + '.jpg') for i in range(1, NUM_IMAGES+1))
# dataset = tf.data.Dataset.from_tensor_slices(file_names)
# print(dataset)
# dataset = dataset.map(lambda x: file_name_to_img(x.b))
# print(list(dataset.as_numpy_iterator()))
# for element in dataset:
#  print(element)
#  print(type(element))
