from tensorflow.keras.datasets import mnist
import numpy as np 
import matplotlib.pyplot as plt 
import cv2

from sklearn.utils import shuffle
from imutils import build_montages

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

    train = make_pairs(trainX[:20], trainY[:20])
    test = make_pairs(testX, testY)
    return train,test



def plot_dataset(data,size=49):
    pairImages = data[0]
    labels = data[1]
    images = []
    for i in np.random.choice(np.arange(0,len(pairImages)),size=49):
        imageA = pairImages[i][0][...,0]
        imageB = pairImages[i][1][...,0]
        label = labels[i]

        output = np.zeros((36, 60), dtype="uint8")
        pair = np.hstack([imageA, imageB])
        output[4:32, 0:56] = pair

        text = "neg" if label[0] == 0 else "pos"
        color = (255, 0, 0) if label[0] == 0 else (0, 255, 0)

        vis = cv2.merge([output] * 3)

        vis = cv2.resize(vis, (96, 51), interpolation=cv2.INTER_LINEAR)

        cv2.putText(vis, text, (2, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                    color, 2)

        images.append(vis)

    montage = build_montages(images, (96, 51), (7, 7))[0]
    plt.imshow(montage)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    train,test =  get_data()
    plot_dataset(train,size=49)

