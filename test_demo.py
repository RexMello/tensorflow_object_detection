import cv2


cams = ''

with open ('cameras.txt','r') as r:
    cams = r.read()

cams = cams.split(',')

caps = []

for cam in cams:
    if cam.isnumeric():
        caps.append(cv2.VideoCapture(int(cam),cv2.CAP_DSHOW))
    else:
        caps.append(cv2.VideoCapture(cam))

while True:
    frames = []

    for cap in caps:
        ret,frame = cap.read()
        if not ret:
            continue
        frames.append(frame)

    if frames==[]:
        break

    for i,frame in enumerate(frames):
        cv2.imshow('Camera number '+str(i),frame)
    
    cv2.waitKey(20)