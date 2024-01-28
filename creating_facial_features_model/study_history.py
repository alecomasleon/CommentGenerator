import pickle
import matplotlib.pyplot as plt

from CommentGenerator.creating_facial_features_model.global_variables import EPOCHS

with open('history.txt', 'rb') as fp:
    history = pickle.load(fp)

print(history.history)

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(EPOCHS)

plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()