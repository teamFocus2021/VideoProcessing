import os
import cv2

print(cv2.__version__)
video_capture = cv2.VideoCapture('test.mp4')
success, image = video_capture.read()
count = 0
success = True

while success:
    cv2.imwrite(os.getcwd() + "/save_img/frame%d.jpg" % count, image)
    success, image = video_capture.read()
    print('Read a new frame: ', success)
    count += 1
