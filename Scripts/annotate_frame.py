import cv2

size = 0


def mouse_callback(event, x, y, flags, param):
    global size
    global image
    global line
    if event == 1:
        image = cv2.circle(image, (x, y), 12, (0, 255, 0), -1)
        line = line + ' ' + str(x / size) + ' ' + str(y / size)
        cv2.imshow('ROI selector', image)


video_file = '../Evaluation/Participant 01.mp4'
cam = cv2.VideoCapture(video_file)
frame = 0

while True:
    ret, image = cam.read()
    if ret is False:
        break
    line = ''
    line = line + 'Frame_' + str(frame)
    frame = frame + 1
    size = 612
    image = cv2.resize(image, (size, size))

    cv2.imshow('ROI selector', image)
    cv2.setMouseCallback('ROI selector', mouse_callback)

    while True:
        """ Enter: to complete == 13 """
        if cv2.waitKey(1) & 0xff == 13:
            line = line + '\n'
            print(line)
            with open('video_annotate.txt', 'a+') as f:
                f.write(line)
            break
