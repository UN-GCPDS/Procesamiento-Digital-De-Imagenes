from tensorflow.keras.datasets import mnist
import numpy as np
import cv2 
import os 
from glob import glob 


def generate_templates():
    (trainX, trainY), (testX, testY) = mnist.load_data()

    unique_labels = np.unique(trainY)
    labels = trainY
    images = trainX
    root_path = os.path.dirname(__file__)

    for unique_label in unique_labels:
        path = os.path.join(root_path,str(unique_label))
        os.makedirs(path,exist_ok=True)
        idx_class =np.random.choice(np.where(labels== unique_label)[0],size=1)
        for i,idx in enumerate(idx_class):
            path_file = os.path.join(path,f'{i}.png')
            cv2.imwrite(path_file, images[idx])



def load_templates():
    root_path = os.path.dirname(__file__)
    regex = os.path.join(root_path,'*','*.png')
    paths = glob(regex)
    images = np.array([cv2.imread(img,0)[...,None] for img in paths])
    labels = np.array([os.path.normpath(img).split(os.sep)[-2] for img in paths])

    return images, labels 

    



if __name__ == "__main__":
    generate_templates()
    images, labels = load_templates()
    print(images.shape,labels)