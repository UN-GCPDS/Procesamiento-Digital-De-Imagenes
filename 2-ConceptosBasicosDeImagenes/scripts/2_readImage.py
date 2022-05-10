"""Script to take read image from disk and display it 

Usage:
    2_readImage.py <path>
"""
from docopt import docopt

import cv2

def main(path_image):
    image =  cv2.imread(path_image)
    cv2.imshow('image',image)
    cv2.waitKey(0)


if __name__ == "__main__":
    args = docopt(__doc__)
    path_image = args['<path>']
    main(path_image)