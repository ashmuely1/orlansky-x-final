import cv2
import time
from selenium import webdriver
from Tkinter import *



CHROME_PATH = r'C:\Users\Administrator\startmenu\Desktop\nand2tetris\chromedriver.exe'

def main2():
    quit()

def main():
    url = raw_input('Please enter the relevant url: ')
    vc = cv2.VideoCapture(0)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
        time.sleep(2)
    else:
        rval = False

    while rval:
        rval, frame = vc.read()
        frame1 = frame
        time.sleep(0.5)
        rval, frame = vc.read()
        frame2 = frame
        frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        frame1 = cv2.GaussianBlur(frame1, (21, 21), 0)
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        frame2 = cv2.GaussianBlur(frame2, (21, 21), 0)
        counter = 0
        [height, width] = frame1.shape
        keki1 = (int(frame1[300, 300]))
        print keki1
        keki2 = (int(frame2[300, 300]))
        print keki2
        print "deduction: " + str(keki1 - keki2)
        print "================================"
        if (keki1 - keki2) > 80 or (keki2 - keki1) > 80:
            driver = webdriver.Chrome(CHROME_PATH)
            driver.get(url)
            main2()
            if key == 27: # exit on ESC
                key = cv2.waitKey(20)
        time.sleep(0.5)

main()
