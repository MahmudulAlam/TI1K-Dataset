import cv2

i = 0
cam = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cam.read()
    if ret is False:
        break
    frame = cv2.resize(frame, (640, 480))
    # matrix = cv2.getRotationMatrix2D((320, 240), 180, 1.0)
    # frame = cv2.warpAffine(frame, matrix, (640, 480))
    cv2.imwrite('../Evaluation/output/Frame_' + str(i) + '.jpg', frame)
    i = i + 1

cam.release()
