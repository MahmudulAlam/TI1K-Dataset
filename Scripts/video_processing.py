import cv2

video_file = 'Participant 01.mp4'
cam = cv2.VideoCapture('../Evaluation/' + video_file)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../Evaluation/processed.mp4', fourcc, 30.0, (640, 480))

initial_frame = 0
counter = 0

while True:
    ret, frame = cam.read()
    print('Frame: ', initial_frame)
    if ret is False:
        break
    if initial_frame >= 100:
        frame = cv2.resize(frame, (640, 480))
        # matrix = cv2.getRotationMatrix2D((320, 240), 180, 1.0)
        # frame = cv2.warpAffine(frame, matrix, (640, 480))
        out.write(frame)
        counter = counter + 1
    initial_frame = initial_frame + 1
    if counter == 301:
        break
    print('Frames: ', initial_frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()
