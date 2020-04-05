import os
import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('processed.mp4', fourcc, 30.0, (1366, 597))

folder_name = 'Screenshots/'
images = os.listdir(folder_name)

for i, image in enumerate(images, 1):
    print('Frame: ', i)
    frame = cv2.imread('Screenshots/' + image)
    frame = cv2.resize(frame, (1366, 597))
    video.write(frame)

video.release()
print('Completed!')
