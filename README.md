# yolo_pandas

In this AI/ML project, we delve into two pivotal research papers that focus on object detection in images using the You Only Look Once (YOLO) methodology. The first paper outlines the foundational YOLO approach, while the second paper introduces enhancements to elevate the YOLO framework's performance.

The links to the papers are:
- https://arxiv.org/pdf/1506.02640.pdf
- https://arxiv.org/pdf/1612.08242.pdf

Our primary objective is to translate the concepts from these research papers into practical computer programs capable of detecting objects within images. Our initial focus centers on implementing the original YOLO method, which involves using a CNN based on the GoogLeNet model for feature extraction and then directly predicting spatially separated bounding boxes and associated class probabilities. This method is renowned for its speed and simultaneous object detection capabilities, making it applicable to a wide range of applications. We will use the PASCAL VOC 2007 and VOC 2012 datasets to train and test our model.

# Functions

## 1. IOU (Intersection over Union)

The IOU function measures localization accuracy and calculates localization errors in object detection models. To calculate IOU, find the intersecting area between the bounding boxes of a prediction and the ground truth. Calculate the total area covered by the two bounding boxes (Union). The ratio of Intersection to Union provides an estimate of how close the bounding box is to the original prediction.

## 2. MAP (Mean Average Precision)

Average Precision is calculated as the area under a precision vs recall curve for a set of predictions. Recall is the ratio of total predictions to existing labels for a class, while Precision is the ratio of true positives to total predictions. The area under the precision vs recall curve gives the Average Precision per class. The Mean Average Precision (MAP) is the mean of these values over all classes.

## 3. NMS (Non-Maximum Suppression)

Objects often fall within one grid, leading to redundant boxes. NMS discards bounding boxes with high overlap, retaining the one with the highest confidence.

## 4. YOLO Loss

(No detailed explanation provided)

# Models

We trained the dataset using the following backbone models, employing augmentations, batch normalization, and parameter tuning:

1. Resnet50
2. Resnet152
3. Googlenet
4. Vgg-19


