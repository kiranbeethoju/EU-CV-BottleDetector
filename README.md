# EU-CV-BottleDetector - Two solutions

### Solution 1_a
1_a: Bottle detector solution ipynb, open it on colab and run the inference cell(before that import the required libraries and run the cell which is responsible to clone required repo)

We can build a simple object detection system using cv2 template matching, but I trust Yolov5, previously I build had done similar object detection project for mask detection using yolov3, but now I used YoloV5 for this demo project.

- Prepared training set with 47 images(annotated with LabelImg)
- val set contains 3 images.


#### Challeges it can tackle
It can detect red labelled dr.pepper bottles and almost all fanta bottles
### Before
<img src="https://github.com/kiranbeethoju/EU-CV-BottleDetector/blob/975ac481c24fc0482410d983a7678ca9afb95bb8/detectTheBottles/testImg.png" width="1000"></a>
&nbsp;
<br>
### After
<img src="https://github.com/kiranbeethoju/EU-CV-BottleDetector/blob/975ac481c24fc0482410d983a7678ca9afb95bb8/detectTheBottles/detected.jpg" width="1000"></a>
&nbsp;
### Metrics 

2 classes 0.659 mAP@0.5

f - mAP 0.373

d - mAP 0.945

### Credits
Thanks to P.J.Reddie and Ultralytics
YoloV3, YoloV5 


### Solution 1_b
1_b: Solution 
It works as expected.

### Before
<img src="https://github.com/kiranbeethoju/EU-CV-BottleDetector/blob/main/Solution-1_b/Task-1b.png" width="1000"></a>
&nbsp;
<br>
### After
<img src="https://github.com/kiranbeethoju/EU-CV-BottleDetector/blob/main/Solution-1_b/Task-1b_Output.png" width="1000"></a>

&nbsp;

