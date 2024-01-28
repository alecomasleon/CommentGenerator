import pickle

models = ['model.txt']

with open('modelMSE.txt', 'rb') as fp:
    model = pickle.load(fp)

model.save('model.keras')
