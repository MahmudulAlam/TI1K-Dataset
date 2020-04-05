import os
import cv2

image_name = 'TI1K_IMAGE_0123.jpg'
folder_name = '../train/'
annotation_file = '../annotation/label.txt'

f = open(annotation_file)
lines = f.readlines()
f.close()

files = os.listdir(folder_name)

for line in lines:
    line = line.strip().split()
    name = line[0]
    if image_name == name:
        print(name)
        line = line[1:]
        for i in range(0, len(line), 2):
            line[i] = int(float(line[i]) * 640)
            line[i + 1] = int(float(line[i + 1]) * 480)
        image = cv2.imread(folder_name + name)
        image = cv2.resize(image, (640, 480))
        image = cv2.rectangle(image, (line[0], line[1]), (line[2], line[3]), (255, 0, 0), 4)
        image = cv2.circle(image, (line[4], line[5]), 12, (0, 0, 255), -10)
        image = cv2.circle(image, (line[6], line[7]), 12, (0, 255, 0), -10)
        cv2.imshow('Visualize Image', image)
        if cv2.waitKey(0) & 0xff == 27:
            break
