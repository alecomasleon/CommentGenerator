import keras
import numpy as np
from cv2 import resize, imread

from CommentGenerator.creating_facial_features_model.global_variables import PATH_TO_IMAGES


class BatchGenerator(keras.utils.Sequence):
    def __init__(self, image_filenames, y, batch_size):
        self.image_filenames = image_filenames
        self.y = y
        self.batch_size = batch_size

    def __len__(self):
        return (np.ceil(len(self.image_filenames) / float(self.batch_size))).astype(int)

    def __getitem__(self, idx):
        batch_x = self.image_filenames[idx * self.batch_size: (idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size: (idx + 1) * self.batch_size]

        # print(batch_x)
        # print()

        return np.array([resize(imread(str(file_name)), (256, 256)) for file_name in batch_x]) / 255.0, np.array(batch_y)
