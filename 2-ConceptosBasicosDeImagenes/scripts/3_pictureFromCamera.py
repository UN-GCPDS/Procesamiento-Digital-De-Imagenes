"""Script to take pictures from camera  

Usage:
    3_pictureFromCamera.py -f FOLDER [-p PATH]

Options:
    -f FOLDER   Path to folder to save images.
    -p PATH     Path or index to camera or video [default: 0]
"""
from docopt import docopt


from datetime import datetime
import os 
import cv2 



def main(path,folder):

    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        
        ret,frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            cv2.imshow('main',frame)

        key = cv2.waitKey(25) 
        if key  == ord('q'):
            break
        elif key == ord('s'):
            filename =  datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
            filename = os.path.join(folder,filename) + '.png'
            cv2.imwrite(filename,frame)
            print(f'Image Save: {filename}')


    cap.release()    
    cv2.destroyAllWindows()


if __name__ == "__main__":

    arguments = docopt(__doc__)
    path = arguments['-p']
    folder = arguments['-f']
    
    if path == '0':
        path = 0 

    main(path,folder)
