import pickle
import matplotlib.pyplot as plt

from CommentGenerator.creating_facial_features_model.global_variables import EPOCHS

EPOCHS = 4

with open('historyMSE.txt', 'rb') as fp:
    history = pickle.load(fp)

print(history.history)

lst = list(history.history.keys())
lst = lst[:len(lst)//2]
for i in range(len(lst)):
    plt.figure(i)

    epochs_range = range(EPOCHS)

    key = lst[i]
    vals = history.history[key]
    plt.plot(epochs_range, vals, label=key)

    key1 = 'val_' + lst[i]
    vals = history.history[key1]
    plt.plot(epochs_range, vals, label=key1)

    plt.legend(loc='upper right')
    plt.title(key + ' and ' + key1)

plt.show()
