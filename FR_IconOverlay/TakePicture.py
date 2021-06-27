# -*- coding: utf-8 -*-
import cv2
import sys
import datetime

imagePath = 'input3.png'

CAM_ID = 0
camid = CAM_ID

# 윈도우 사용자는 마지막에 cv2.CAP_DSHOW 추가
cam = cv2.VideoCapture(camid)  # , cv2.CAP_DSHOW

if cam.isOpened() == False:
    print ('cant open the cam (%d)' % camid)

p_start = datetime.datetime.now()

while (datetime.datetime.now() - p_start).seconds < 1:
    ret, frame = cam.read()

if frame is None:
    print ('frame is not exist')

cv2.imwrite(imagePath, frame)
cam.release()

print("Finished!")
