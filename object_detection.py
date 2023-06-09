import cv2

configPath = 'object_detection_models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'object_detection_models/frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def detect_object_from_input(image,id=1):
    classIds, confs, bbox = net.detect(image,confThreshold=0.6)

    leftt = topp = rightt = bottomm = 0
    person_found = False

    if len(classIds) != 0:
        for classId, _,box in zip(classIds.flatten(),confs.flatten(),bbox):
            if classId == id:
                person_found = True
                leftt = box[0]
                topp = box[1]

                rightt = leftt+box[2]
                bottomm = topp+box[3]

                cv2.rectangle(image,box,color=(0,255,0),thickness=2)

    

    return image,person_found, (topp,bottomm,leftt,rightt)


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,frame = cap.read()

    frame,_,_ = detect_object_from_input(frame)
    cv2.imshow('output',frame)
    cv2.waitKey(1)