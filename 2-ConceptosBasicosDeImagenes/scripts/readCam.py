import cv2 


def main():

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        
        ret,frame = cap.read()
        cv2.imshow('main',frame)

        if cv2.waitKey(1) == ord('q'):
            break 
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
