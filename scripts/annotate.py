import os
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


folder_name = '../train/'

for image_name in os.listdir(folder_name):
    line = ''
    line = line + image_name
    image = cv2.imread(folder_name + image_name)
    size = 612
    image = cv2.resize(image, (size, size))
    x, y, h, w = cv2.selectROI(image, fromCenter=False)
    tl = (x, y)
    br = (x + h, y + w)
    line = ' ' + line + ' ' + str(tl[0] / size) + ' ' + str(tl[1] / size) + \
           ' ' + str(br[0] / size) + ' ' + str(br[1] / size)
    image = cv2.rectangle(image, tl, br, (255, 0, 0), 2)
    cv2.imshow('ROI selector', image)
    cv2.setMouseCallback('ROI selector', mouse_callback)

    while True:
        """ Enter: to complete == 13 """
        if cv2.waitKey(1) & 0xff == 13:
            line = line + '\n'
            print(line)
            with open('annotate.txt', 'a+') as f:
                f.write(line)
            break
