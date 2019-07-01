from __future__ import print_function

import argparse

import cv2

from facedetector import FaceDetector

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-f', '--face', required=True, help='Path to where the face cascade resides.')
argument_parser.add_argument('-i', '--image', required=True, help='Path to where the image file resides.')
arguments = vars(argument_parser.parse_args())

image = cv2.imread(arguments['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_detector = FaceDetector(arguments['face'])
face_rectangles = face_detector.detect(gray, scale_factor=1.2, min_neighbors=5, min_size=(30, 30))
print('I found {} faces.'.format(len(face_rectangles)))

green = (0, 255, 0)
thickness = 2
for (x, y, width, height) in face_rectangles:
    cv2.rectangle(image, (x, y), (x + width, y + height), green, thickness)

cv2.imshow('Faces', image)
cv2.waitKey(0)
