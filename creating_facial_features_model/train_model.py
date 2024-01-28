import pickle

import tensorflow as tf
from keras import Sequential, Model
from keras.layers import Dense, Input, Conv2D, Concatenate, Flatten
from keras import layers, optimizers
import numpy as np
import pandas as pd
from keras.src.callbacks import ModelCheckpoint
from keras.src.losses import CategoricalCrossentropy

from CommentGenerator.creating_facial_features_model.BatchGenerator import BatchGenerator
from CommentGenerator.creating_facial_features_model.global_variables import PATH_TO_ALL_DATA, PATH_TO_IMAGES, \
    NUM_IMAGES, START_VAL, START_TEST, EPOCHS
from CommentGenerator.creating_facial_features_model.preprocess import file_name_to_img

if True:
    optimizer = optimizers.Adam()
    print(optimizer)
    model = Sequential([
        layers.Rescaling(1. / 255, input_shape=(256, 256, 3)),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(40, activation='sigmoid')
    ])

    loss = CategoricalCrossentropy(label_smoothing=0.09)
    model.compile(optimizer=optimizer, loss=loss)

    batch_size = 40

    x_train_filenames = list(PATH_TO_IMAGES + '{:06d}'.format(i+1) + '.jpg' for i in range(0, START_VAL))
    x_val_filenames = list(PATH_TO_IMAGES + '{:06d}'.format(i+1) + '.jpg' for i in range(START_VAL, START_TEST))

    y_train = pd.read_csv(PATH_TO_ALL_DATA + 'list_attr_celeba.csv')
    y_train = y_train.drop('filename', axis=1)

    my_training_batch_generator = BatchGenerator(x_train_filenames, y_train[0:START_VAL], batch_size)
    my_validation_batch_generator = BatchGenerator(x_val_filenames, y_train[START_VAL:START_TEST], batch_size)

    checkpoint = ModelCheckpoint('modelPSN_checkpoint.txt', monitor="val_loss", save_best_only=True, save_weights_only=False)

    history = model.fit_generator(generator=my_training_batch_generator,
                                  steps_per_epoch=START_VAL//batch_size,
                                  epochs=EPOCHS,
                                  verbose=1,
                                  validation_data=my_validation_batch_generator,
                                  validation_steps=(START_TEST-START_VAL)//batch_size,
                                  callbacks=[checkpoint])

    print(history)
    print(model)

    with open('model.txt', 'wb') as fp:
        pickle.dump(model, fp)

    with open('history.txt', 'wb') as fp:
        pickle.dump(history, fp)