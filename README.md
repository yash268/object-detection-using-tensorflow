# object-detection-using-tensorflow
object detection using tensorflow and imageAI

Object detection is a technology that falls under the broader domain of Computer Vision. It deals with identifying and tracking objects present in images and videos. Object detection has multiple applications such as face detection, vehicle detection, pedestrian counting, self-driving cars, security systems, etc.

The two major objectives of object detection include:

• To identify all objects present in an image
• Filter out the object of attention

In this article, you will see how to perform object detection in Python with the help of the ImageAI library.

--> Setting up your Environment

In this part of the tutorial, we will work through the installation of ImageAI.

To use ImageAI you need to install a few dependencies. The first step is to have Python installed on your computer. Download and install Python 3 from the official Python website.

Once you have Python installed on your computer, install the following dependencies using pip:

• TensorFlow

$ pip install tensorflow

• OpenCV

$ pip install opencv-python

• Keras

$ pip install keras

• ImageAI

$ pip install imageAI


Now download the TinyYOLOv3 model file that contains the classification model that will be used for object detection.
link:https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5  And put that model into models folder.


Our first task here is to create the necessary folders. For this tutorial we need the following folders:

• Object detection: root folder
    • models: stores pre-trained model
    • input: stores image file on which we want to perform object detection
    • output: stores image file with detected objects
    
    
Now run the detect.py file in command prompt and wait for the output, the detected object is highlighted by squre in image which is stored on output folder.


