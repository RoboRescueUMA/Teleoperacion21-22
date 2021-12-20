# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:49:08 2021

@author: Fernando Gómez de la Varga   Github: fer5899
"""

from __future__ import print_function

import cv2

def video(videoFile):
    # open video file and get basic information

    cap = cv2.VideoCapture(videoFile)
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open video file")
    
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame,None,fx=1,fy=1)    # the processing is done
                                                    # frame by frame
        cv2.imshow('Input', frame)
    
        c = cv2.waitKey(1)  # waits a minimum of 1 ms before continuing
        if c == 27:   # if key 27 (code for escape key) is pressed the video stops
            break
    
    cap.release()
    cv2.destroyAllWindows()


def main():
    filePath = "D:\IMG_2484.mov"
    video(filePath)

if __name__ == "__main__":
    main()