# importing libraries
import cv2
import numpy as np
import dlib

# function to convert dlib.full_object_detection to numpy array
def shape_to_np(shape, dtype="int"):
	coords = np.zeros((68, 2), dtype=dtype)
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	return coords

# reading an image and converting it to grayscale
image = cv2.imread('johny.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# loading the classifiers with respected files
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=5)

# looping through each detected faces and drawing rectangle around the face and circles around the feature points
if len(faces)>0:
    for x,y,w,h in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0),3)
	# creating the rectangle object from the outputs of haar cascade calssifier
        drect = dlib.rectangle(int(x),int(y),int(x+w),int(y+h))
        landmarks = predictor(gray, drect)
        points = shape_to_np(landmarks)
        for i in points:
            x = i[0]
            y = i[1]
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

cv2.imshow('image',image)
