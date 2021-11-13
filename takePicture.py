#! /usr/bin/python

from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import RPi.GPIO as GPIO

RELAY = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY,GPIO.LOW)

def takePicture():

        name = "unrecognized"
        #Determine faces from encodings.pickle
        encodingsP = "/home/pi/CSC132-Final/encodings.pickle"
        #https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
        cascade = "/home/pi/.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml"

        data = pickle.loads(open(encodingsP, "rb").read())
        detector = cv2.CascadeClassifier(cascade)

        # initialize the video stream and allow the camera sensor to warm up
        vs = VideoStream(src=0).start()
        #vs = VideoStream(usePiCamera=True).start()
        time.sleep(2.0)

        # start the FPS counter
        fps = FPS().start()

        # set default door value
        doorUnlock = False

        # grab the frame from the threaded video stream and resize it
        # to 500px (to speedup processing)
        frame = vs.read()
        frame = imutils.resize(frame, width=500)

        # convert the input frame from (1) BGR to grayscale (for face
        # detection) and (2) from BGR to RGB (for face recognition)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # detect faces in the grayscale frame
        rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                minNeighbors=5, minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE)

        # reorder coordinates to top, right, bottom, left
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

        # view each face in bounding box
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
                # attempt to match each face
                matches = face_recognition.compare_faces(data["encodings"],encoding)
        
                # check to see if we have found a match
                if True in matches:
                        # find the indexes of all matched faces then initialize a
                        # dictionary to count the total number of times each face
                        # was matched
                        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}
                        
                        # to unlock the door
                        doorUnlock = True
                       
        # do a bit of cleanup
        vs.stop()

        return doorUnlock

def unlockDoor():
        GPIO.output(RELAY,GPIO.HIGH)

def lockDoor():
        GPIO.output(RELAY,GPIO.LOW)
