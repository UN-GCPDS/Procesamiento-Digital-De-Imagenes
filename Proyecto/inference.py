from tensorflow.keras.models import load_model 
import cv2 
import numpy as np
import matplotlib.pyplot as plt 


from model import uclidean_distance
from templates.templates import load_templates


def get_result(labels,results):
    results = np.squeeze(results)
    unique_labels = np.unique(labels)
    prom = [np.mean(results[labels == label]) for label in unique_labels]
    idx_result = np.argmax(prom)
    result_prop = prom[idx_result]
    result_class = unique_labels[idx_result]
    return result_class, result_prop

def run_with_camera():

    images, labels = load_templates()
    model = load_model('trainedmodel.h5',custom_objects={'Cosine_Distance':uclidean_distance})
    imagesA = images 

    cap = cv2.VideoCapture(0)


    while cap.isOpened():
        ret,frame = cap.read()
        if ret:

            img = cv2.resize(frame,(28,28))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            imagesB = np.array([img]*len(images))
    
            results = model.predict((imagesA,imagesB))
            result_class, result_prop = get_result(labels,results)

            frame = cv2.putText(img = frame,
                                text = f'Class: {result_class}, Prop: {result_prop:.2f}',
                                org = (0, 25),
                                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                                fontScale = 1,
                                color = (0, 0, 255),thickness = 1)

            cv2.imshow('result', frame)


        key = cv2.waitKey(1) 
        if key  == ord('q'):
            break


def run_one_img(img):
    images, labels = load_templates()
    model = load_model('trainedmodel.h5',custom_objects={'Cosine_Distance':uclidean_distance})
    imagesA = images 

    imagesB = np.array([img]*len(images))
    results = model.predict((imagesA,imagesB))
    result_class, result_prop = get_result(labels,results) 
    
    plt.imshow(img)
    plt.title(f'Class: {result_class}, Prop: {result_prop:.2f}')
    plt.show()



if __name__ == "__main__":
    img = cv2.imread('./templates/9/0.png',0)[...,None]
    run_one_img(img)
    #run_with_camera()