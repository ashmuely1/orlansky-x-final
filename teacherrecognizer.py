import numpy as np
import cv2

def main():
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        cascPath = "C:\Users\Administrator\startmenu\Desktop\Real Time Face Recognition Using OpenCV and MATLAB\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        faces = faceCascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
        cv2.imshow('frame',frame)
        if cv2.w
        10.
        `aitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()