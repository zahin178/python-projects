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
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
detector = dlib.get_frontal_face_detector()
faces = detector(gray)

# looping through each detected faces and drawing rectangle around the face and circles around the feature points
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 220), 3)
    landmarks = predictor(gray, face)
    points = shape_to_np(landmarks)
    for i in points:
        x = i[0]
        y = i[1]
        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

cv2.imshow('image',image)
