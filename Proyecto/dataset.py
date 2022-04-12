from tensorflow.keras.datasets import mnist
import numpy as np 
from sklearn.utils import shuffle

def make_pairs(images,labels):
    pairImages = []
    pairLabels = []

    numClasses = len(np.unique(labels))
    idx = [np.where(labels== i)[0] for i in range(0,numClasses)]

    for idxA in range(len(images)):
        currentImage = images[idxA]
        label = labels[idxA]

        idxB = np.random.choice(idx[label])
        posImage = images[idxB]

        pairImages.append([currentImage,posImage])
        pairLabels.append([1])

        negIdx = np.where(labels!=label)[0]
        negImage = images[np.random.choice(negIdx)]

        pairImages.append([currentImage,negImage])
        pairLabels.append([0])

    
    pairImages = np.array(pairImages)[...,None]
    pairLabels = np.array(pairLabels)
    X, y = shuffle(pairImages, pairLabels, random_state=42)

    return X, y


def get_data():
    (trainX, trainY), (testX, testY) = mnist.load_data()

    train = make_pairs(trainX, trainY)
    test = make_pairs(testX, testY)
    return train,test


if __name__ == '__main__':
    train,test =  get_data()
