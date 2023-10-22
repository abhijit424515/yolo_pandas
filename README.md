# yolo_pandas

In this AI/ML project, we delve into two pivotal research papers that focus on object detection in images using the You Only Look Once (YOLO) methodology. The first paper outlines the foundational YOLO approach, while the second paper introduces enhancements to elevate the YOLO framework's performance.

The links to the papers are:
- https://arxiv.org/pdf/1506.02640.pdf
- https://arxiv.org/pdf/1612.08242.pdf

Our primary objective is to translate the concepts from these research papers into practical computer programs capable of detecting objects within images. Our initial focus centers on implementing the original YOLO method, which involves using a CNN based on the GoogLeNet model for feature extraction and then directly predicting spatially separated bounding boxes and associated class probabilities. This method is renowned for its speed and simultaneous object detection capabilities, making it applicable to a wide range of applications. We will use the PASCAL VOC 2007 and VOC 2012 datasets to train and test our model.

Subsequently, we investigate the advancements introduced in the second research paper to implement the model YOLOv2, which further refines the YOLO methodology to enhance its effectiveness in object detection tasks. Certain improvements from the original model include a hierarchial classification scheme instead of a single-level classification, replacing the original CNN with a new one based on the lighter model Darknet-19, using k-means to determine anchor boxes instead of manual selection, and various training techniques like batch normalization, resolution training, etc. We will additionally use the COCO dataset for training and testing the YOLOv2 model
