# TI1K-Dataset
The dataset has been used in [Finger gesture-based Mixed Reality interaction system](http:// ) in the egocentric vision where real-time fingertip 
detection and tracking system is introduced. If you are interested, please visit the project GitHub page. 

## Dataset-Description
Thumb Index 1000 (TI1K) is a dataset of 1000 hand images with the hand bounding box, and thumb and index fingertip positions. 
The dataset includes the natural movement of thumb and index fingers making it suitable for mixed reality (MR) applications. 

The dataset contains images only with the thumb and index fingers of both hands of resolution 640x480. All the annotations of the
training and test images are in the "label.txt" file in the Annotation folder. The format of the annotation is: 

[name of the image, xtl, ytl, xbr, ybr, xt, yt, xi, yi]

* xtl = x coordinate of the top left corner of the hand bounding box 
* ytl = y coordinate of the top left corner of the hand bounding box 
* xbr = x coordinate of the bottom right corner of the hand bounding box
* ybr = y coordinate of the bottom right corner of the hand bounding box
* xt = x coordinate of the thumb 
* yt = y coordinate of the thumb 
* xi = x coordinate of the index 
* yi = y coordinate of the index 

*All the values are normalized. 

## Example Image of the Dataset
Here is a sample image from the dataset along with its ground truth annotation:
<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/54509941-974e4080-4975-11e9-8da6-946d1ce23b29.jpg" width="320">
  <img src="https://user-images.githubusercontent.com/37298971/54509952-a33a0280-4975-11e9-8a3f-c0fb771f5791.jpg" width="320">
</p>

The total dataset is split into two parts. Among 1000 images, 900 images are for the training set and 100 images for the test set.  

## Evaluation 
For evaluation purpose of the real-time fingertip detection and tracking system, real-time video of both left- and right-hand 
fingers have been taken. Evaluation folder contains four videos of the hand finger movement of the four participants. 
All the video file in the '.mp4' format contains 301 frame sequence with resolution 640x480 at 30 frames per second. 
Here, one extra frame is taken to initialize the tracker. The annotations of the thumb and index fingertip are in the 
Annotation/Evaluation folder. The four text files contain the annotations of the four videos of the 301 frame sequences. 
The format of the annotation is:

[frame number, xt, yt, xi, yi]

* xt = x coordinate of the thumb 
* yt = y coordinate of the thumb 
* xi = x coordinate of the index 
* yi = y coordinate of the index
