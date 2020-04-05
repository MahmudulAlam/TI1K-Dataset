import os
import cv2

user = 1
transformation = 'translation'
video_file = '../evaluation/' + transformation + '/' + str(user) + '.mp4'
output_folder = '../evaluation/output/'

try:
    os.mkdir(output_folder)
except FileExistsError:
    pass
annotation_file = '../evaluation/' + transformation + '/' + transformation + '_' + str(user) + '.txt'

f = open(annotation_file)
lines = f.readlines()
f.close()

cam = cv2.VideoCapture(video_file)
frame = 1

while True:
    ret, image = cam.read()

    if ret is False:
        break

    for line in lines:
        line = line.strip().split()
        name = line[0]
        line = line[1:]
        if name == 'Frame_' + str(frame):
            for i in range(0, len(line), 2):
                line[i] = int(float(line[i]) * 640)
                line[i + 1] = int(float(line[i + 1]) * 480)

            print(frame)
            image = cv2.rectangle(image, (line[0], line[1]), (line[2], line[3]), (255, 0, 0), 2)
            image = cv2.circle(image, (line[4], line[5]), 12, (0, 0, 255), -10)
            image = cv2.circle(image, (line[6], line[7]), 12, (0, 255, 0), -10)
            cv2.imwrite(output_folder + name + '.jpg', image)
            frame = frame + 1
            break

cam.release()
