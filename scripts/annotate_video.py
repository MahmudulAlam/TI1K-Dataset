import cv2

size = 0


def mouse_callback(event, x, y, flags, param):
    global size
    global image
    global line
    if event == 1:
        image = cv2.circle(image, (x, y), 12, (0, 255, 0), -1)
        line = line + ' {0:.7f} {1:.7f}'.format(x / size, y / size)
        cv2.imshow('ROI selector', image)


user = 1
transformation = 'scale'
video_file = '../evaluation/' + transformation + '/' + str(user) + '.mp4'
cam = cv2.VideoCapture(video_file)
frame = 0
count = 1

while True:
    ret, image = cam.read()

    if ret is False:
        break

    name = 'Frame_' + str(count)
    count = count + 1
    size = 612
    image = cv2.resize(image, (size, size))
    x, y, h, w = cv2.selectROI(image, fromCenter=False)
    tl = (x, y)
    br = (x + h, y + w)
    line = '{0} {1:.7f} {2:.7f} {3:.7f} {4:.7f}'.format(name, tl[0] / size, tl[1] / size, br[0] / size, br[1] / size, 6)

    image = cv2.rectangle(image, tl, br, (255, 0, 0), 2)
    cv2.imshow('ROI selector', image)
    cv2.setMouseCallback('ROI selector', mouse_callback)

    while True:
        """ Enter: to complete == 13 """
        if cv2.waitKey(1) & 0xff == 13:
            line = line + '\n'
            print(line)
            with open('../evaluation/' + transformation + '_' + str(user) + '.txt', 'a+') as f:
                f.write(line)
            break
