import os
import cv2

user = 1
transformation = 'translation'
cam = cv2.VideoCapture('../evaluation/' + transformation + '/' + str(user) + '.mp4')

if not os.path.exists('../evaluation/output/'):
    os.makedirs('../evaluation/output/')

i = 0
while True:
    ret, image = cam.read()

    if ret is False:
        break

    cv2.imwrite('../evaluation/output/image_' + str(i) + '.jpg', image)
    i = i + 1
    print(i)

cam.release()
