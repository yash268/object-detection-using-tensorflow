from imageai.Detection import ObjectDetection

import time

list = []

detector = ObjectDetection()

model_path = "./models/yolo-tiny.h5"
input_path = "./input/test46.jpg"
output_path = "./output/output.jpg"

detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

for eachItem in detection:
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])
    list.append(eachItem["name"])

x = list.count("car")

print("\n\ncar:" ,x)

y = list.count("person")

print("person:" ,y)




z  = x + y



def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1


if z==0:
	print("Lane is Free!")

if y>=1:
	print("LED1 and LED2 are ON!!!!!")
	countdown(20)
	print("\n\n\nLED1 and LED2 are OFF!!!!")

if x>=1:
	print("LED1 , LED2 , LED3 ,LED4 are ON!!!!")
	countdown(5)
	print("\n\n\nLED1 , LED2 , LED3 ,LED4 are OFF!!!!")





