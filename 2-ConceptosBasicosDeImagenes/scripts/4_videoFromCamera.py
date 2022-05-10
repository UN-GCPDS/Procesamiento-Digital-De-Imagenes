"""Script to take pictures from camera  

Usage:
    4_videoFromCamera.py [-n NAME -p PATH]

Options:
    -n NAME     Name for the video output [default: output.mp4]
    -p PATH     Path or index to camera or video [default: 0]
"""
from docopt import docopt
import cv2 


def main(path,name):

    cap = cv2.VideoCapture(path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 20.0
    out = cv2.VideoWriter(name, fourcc, fps, (640,  480))

    while cap.isOpened():
        
        ret,frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            cv2.imshow('main',frame)
            out.write(frame)

        key = cv2.waitKey(1) 
        if key  == ord('q'):
            break


    cap.release()    
    cv2.destroyAllWindows()


if __name__ == "__main__":

    arguments = docopt(__doc__)
    path = arguments['-p']
    name = arguments['-n']
    
    if path == '0':
        path = 0 

    main(path,name)
