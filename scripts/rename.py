import os
import cv2

i = 1

for image_file in os.listdir('Images/'):
    image = cv2.imread('Images/' + image_file)
    image = cv2.resize(image, (640, 480))
    cv2.imwrite('Hall1_' + str(i) + '.jpg', image)
    # os.rename('Batch2/' + image, 'Batch2/image_'+str(i)+'.jpg')
    i = i + 1
