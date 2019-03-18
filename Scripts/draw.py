import os
import cv2

participant_id = 1
video_file = '../Evaluation/Participant 0' + str(participant_id) + '.mp4'
output_folder = '../Evaluation/output/'
try:
    os.mkdir(output_folder)
except FileExistsError:
    pass
annotation_file = '../Annotation/Evaluation/Participant 0' + str(participant_id) + '.txt'

f = open(annotation_file)
lines = f.readlines()
f.close()

cam = cv2.VideoCapture(video_file)
frame = 0

while True:
    ret, image = cam.read()
    if ret is False:
        break
    for line in lines:
        line = line.strip().split()
        name = line[0]
        frame_name = 'Frame_' + str(frame)
        if frame_name == name:
            print(name)
            line = line[1:]
            for i in range(0, len(line), 2):
                line[i] = int(float(line[i]) * 640)
                line[i + 1] = int(float(line[i + 1]) * 480)
            image = cv2.circle(image, (line[0], line[1]), 12, (0, 0, 255), -10)
            image = cv2.circle(image, (line[2], line[3]), 12, (0, 255, 0), -10)
            cv2.imwrite(output_folder + name + '.jpg', image)
            frame = frame + 1
            break

cam.release()
