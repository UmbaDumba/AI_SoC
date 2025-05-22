
import torch
import cv2

title = "yolo_result"

img_url = '/home/pi/Pictures/mycat.jpg'             # 0번 카메라 장치 연결 
origin_img = cv2.imread(img_url)
img = cv2.imread(img_url)

conf = 0.3

def nothing(val):
    # val : confidence * 100
    conf = val / 100.0
    print(conf)

    
    #cv2.imshow(title, img)


model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

r = model(img_url)
r_points = r.pandas().xyxy[0].to_numpy()


cv2.namedWindow(title)
cv2.createTrackbar('conf', title, 0, 100, nothing)


cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결 

if cap.isOpened():                      # 캡쳐 객체 연결 확인
    while True:
        if cv2.waitKey(1) == ord('q'):
                break   
        
        ret, frame = cap.read()           # 다음 프레임 읽기
        if ret:
            r = model(frame)
            r_points = r.pandas().xyxy[0].to_numpy()
            #print(r_points)
            for p in r_points:
                if p[4] > conf:
                    frame = cv2.rectangle(frame, (int(p[0]),int(p[1])), (int(p[2]),int(p[3])), (255,0,0), 5)
                else:
                    pass
            cv2.imshow(title, frame)
            
        else:
            print('no frame')
            break
else:
    print("can't open camera.")



cv2.destroyAllWindows()