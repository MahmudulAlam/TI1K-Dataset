import cv2

cam = cv2.VideoCapture('../Evaluation/138.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ID1.mp4', fourcc, 30.0, (640, 480))
i = 0
c = 0
while True:
    ret, frame = cam.read()
    print(i)
    if ret is False:
        break
    frame = cv2.resize(frame, (640, 480))
    matrix = cv2.getRotationMatrix2D((320, 240), 180, 1.0)
    frame = cv2.warpAffine(frame, matrix, (640, 480))
    out.write(frame)
    i = i + 1
    print('Frames: ', i)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()
