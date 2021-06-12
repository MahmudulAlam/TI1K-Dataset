<h1 align="center">TI1K Dataset :point_up_2::raised_hand_with_fingers_splayed:</h1>

The dataset has been used in [Affine Transformation of Virtual Object](https://github.com/MahmudulAlam/Fingertip-Mixed-Reality) in the egocentric vision where real-time fingertip detection and tracking system is introduced. If you are interested, please visit the GitHub page. The dataset has been developed and updated for the following papers. If you use the dataset, please cite the the papers as

### Paper 

| [![Paper](https://img.shields.io/badge/paper-ScienceDirect-f2862e.svg?longCache=true&style=flat)](https://doi.org/10.1016/j.vrih.2020.10.001) 	|   ![](https://img.shields.io/badge/-v2.0-brightgreen)	| [***```Affine transformation of virtual 3D object using 2D localization of fingertips```***](https://www.sciencedirect.com/science/article/pii/S2096579620300917?via%3Dihub) 🔗 |
|:-:	|:-:	| :-: |

```
@article{alam2020affine,
  title={Affine transformation of virtual 3D object using 2D localization of fingertips},
  author={Alam, Mohammad Mahmudul and Rahman, SM Mahbubur},
  journal={Virtual Reality \& Intelligent Hardware},
  volume={2},
  number={6},
  pages={534--555},
  year={2020},
  publisher={Elsevier}
}
```

|  [![Paper](https://img.shields.io/badge/paper-IeeeXplore-blue.svg?longCache=true&style=flat)](https://ieeexplore.ieee.org/abstract/document/9035256) 	|  ![](https://img.shields.io/badge/-v1.0-brightgreen) 	| [***```Detection and Tracking of Fingertips for Geometric Transformation of Objects in Virtual Environment```***](https://ieeexplore.ieee.org/abstract/document/9035256) 🔗 |
|:-:	|:-:	| :-:	|

```
@inproceedings{alam2019detection,
  title={Detection and Tracking of Fingertips for Geometric Transformation of Objects in Virtual Environment},
  author={Alam, Mohammad Mahmudul and Rahman, SM Mahbubur},
  booktitle={2019 IEEE/ACS 16th International Conference on Computer Systems and Applications (AICCSA)},
  address = {Abu Dhabi, United Arab Emirates},
  pages={1--8},
  year={2019},
  organization={IEEE}
}
```

### Dataset Description
Thumb Index 1000 (TI1K) is a dataset of 1000 hand images with the hand bounding box, and thumb and index fingertip positions. 
The dataset includes the natural movement of thumb and index fingers making it suitable for mixed reality (MR) applications. 

The dataset contains images only with the thumb and index fingers of both hands of resolution ```640x480```. All the annotations of the
training and test images are in the "label.txt" file in the Annotation folder. The format of the annotation is: 

```[name of the image, xtl, ytl, xbr, ybr, xt, yt, xi, yi]```

* xtl = x coordinate of the top left corner of the hand bounding box 
* ytl = y coordinate of the top left corner of the hand bounding box 
* xbr = x coordinate of the bottom right corner of the hand bounding box
* ybr = y coordinate of the bottom right corner of the hand bounding box
* xt = x coordinate of the thumb 
* yt = y coordinate of the thumb 
* xi = x coordinate of the index 
* yi = y coordinate of the index 

*All the values are normalized. 

### Example Image of the Dataset
Here is a sample image from the dataset along with its ground truth annotation:
<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/54509941-974e4080-4975-11e9-8da6-946d1ce23b29.jpg" width="300">
  <img src="https://user-images.githubusercontent.com/37298971/54509952-a33a0280-4975-11e9-8a3f-c0fb771f5791.jpg" width="300">
</p>

The total dataset is split into two parts. Among 1000 images, 900 images are for the training set and 100 images for the test set.  

### Evaluation 
For evaluation purpose of the real-time fingertip detection and tracking system, real-time video of both left- and right-hand fingers have been taken. The evaluation folder contains three folders of four videos of the hand finger movement of the four participants. All the video file in the ```'.mp4'``` format contains 50 frame sequences with resolution 640x480 at 10 frames per second. Each folder contains the corresponding annotations too. The format of the annotation of the videos is as same as the dataset images.
