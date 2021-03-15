# CODE THAT USES THE PRETRAINED CNN MODEL FOR GESTURE RECOGNITION

import pyrealsense2 as rs
import cv2
import imutils
import numpy as np
from sklearn.metrics import pairwise
import os
from keras.datasets import mnist
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
import glob
import time
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

# Main function
if __name__ == "__main__":

    # get the reference to the webcam
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    align_to = rs.stream.color
    alignedFs = rs.align(align_to)
    profile = pipeline.start(config)
    # region of interest (ROI) coordinates
    left, top, right, bottom = 40, 0, 0, 40
    # initialize num of frames
    num_frames = 0

    # calibration indicator
    calibrated = False
    # get rectangle
    run=4
    # keep looping, until interrupted
    while(True):
        # get the current frame 
        frames = pipeline.wait_for_frames()
        aligned_frames = alignedFs.process(frames)
        color_frame = aligned_frames.get_color_frame()  
        #depth_frame = aligned_frames.get_depth_frame()
        frame = np.asanyarray(color_frame.get_data())
        #frame_depth= np.asanyarray(depth_frame.get_data())
        # resize the frame
        frame = imutils.resize(frame, width=640)

        # flip the frame so that it is not the mirror view
        frame = cv2.flip(frame, 1)

        # clone the frame
        clone = frame.copy()

        # get the height and width of the frame
        (height, width) = frame.shape[:2]

        # draw the segmented hand
        
        if(left==640 and top==0):
            run=1
        if(left==640 and bottom==480):
            run=2
        if(right==0 and bottom==480):
            run=3
        if(right==0 and top==0):
            run=4
        for case in switch(run):
            if case(1): 
                top=top+4
                bottom=bottom+4
                break
            if case(2): 
                left=left-4
                right=right-4
                break
            if case(3): 
                top=top-4
                bottom=bottom-4
                break
            if case(4): 
                left=left+4
                right=right+4
                break
            if case(): pass

        cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)

        # increment the number of frames
        num_frames += 1

        # display the frame with segmented hand
        cv2.imshow("Video Feed", clone)

        # observe the keypress by the user
        keypress = cv2.waitKey(1) & 0xFF

        # if the user has pressed "q", then stop looping
        if keypress == ord("q"):
            break

# free up memory
pipeline.stop()
cv2.destroyAllWindows()
