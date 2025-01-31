import os
from django.conf import settings
import cv2 # pip install opencv-python
import matplotlib.pyplot as plt # pip install matplotlib
from collections import Counter

# Path to model files
config_file = os.path.join(settings.BASE_DIR, 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
frozen_model = os.path.join(settings.BASE_DIR, 'frozen_inference_graph.pb')

model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []
with open(os.path.join(settings.BASE_DIR, 'coconames.txt'), 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
print(classLabels)


model.setInputSize(320, 320)
model.setInputScale(1.0/127.5) ## 255/2 = 127.5
model.setInputMean( (127.5, 127.5, 127.5) ) ## moblilenet => [-1, 1]
model.setInputSwapRB(True)
# it will perform automatically. We don't need to convert this each time

def objDetect(image_path):
    img = cv2.imread(image_path)
        
    try:
        # detect objects
        ClassIndex, confidece, bbox = model.detect(img, confThreshold=0.60)
        # print(ClassIndex)
    except Exception:
        if (len(ClassInd)<1):
            return

    font_scale = 2
    font = cv2.FONT_HERSHEY_PLAIN

    for ClassInd, conf, boxes in zip(ClassIndex, confidece, bbox):
        # cv2.rectangle( frame, (x,y), (x+w, y+h)), (255, 0, 0), 2)
        # cv2.putText( img, text, (text_offset_x, text_offset_y), font, fontSclae=font_scale, color(0,0,0), thickness=1 )
        cv2.rectangle(img, boxes, (255, 0, 0), 2) #rectangle color is blue
        cv2.putText(img, classLabels[ClassInd-1], (boxes[0]+10, boxes[1]+30), font, fontScale=font_scale, color=(0, 0, 255), thickness=2)
        
    

    # Save processed image in 'uploads' folder
    # output_path = os.path.join(settings.MEDIA_ROOT, 'uploads', 'img_out.jpeg')
    output_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'img', 'img_out.jpeg')
    cv2.imwrite(output_path, img)
    # cv2.imwrite('uploads/img_out.jpeg', img) # save boxed image (original color)
    
    # outputImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # image boxed to cv2.COLOR_BGR2RGB. Otherwise imshow() shows degraded image.
    # plt.imshow( outputImg ) # see original color

    objects = []
    for i in ClassIndex:
        objects.append(classLabels[i-1].capitalize())  # Capitalizing each object name

    obj_cnt = []
    # Print each object name with its occurrence count
    for object_name, count in Counter(objects).items():
        # print(f"{object_name}: {count}")
        # obj_cnt.append(f"{object_name}: {count}")
        obj_cnt.append([object_name, count])
        
    return obj_cnt, output_path

