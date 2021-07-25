# -*- coding: utf-8 -*-
import cv2
import sys
import datetime

CAM_ID = 0
camid = CAM_ID

# 윈도우 사용자는 마지막에 cv2.CAP_DSHOW 추가
cam = cv2.VideoCapture(camid)  # , cv2.CAP_DSHOW

# 리눅스 사용자는 아래와 같이 사용
# cam = cv2.VideoCapture(camid)
if cam.isOpened() == False:
    print ('cant open the cam (%d)' % camid)

p_start = datetime.datetime.now()

while (datetime.datetime.now() - p_start).seconds < 1:
    ret, frame = cam.read()

if frame is None:
    print ('frame is not exist')

# png로 압축 없이 영상 저장
imagePath = 'saveimage2.jpg'
cv2.imwrite(imagePath, frame)
cam.release()

# Get user supplied values
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

#cv2.imshow("Faces found", image)
#cv2.waitKey(0)
