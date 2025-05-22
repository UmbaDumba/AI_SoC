import torch
import cv2

title = "yolo_result"

def nothing(val):
    # val : confidence * 100
    conf = val / 100.0
    print(conf)
    if r_points[0][4] > conf:
        img = cv2.rectangle(origin_img, (int(r_points[0][0]),int(r_points[0][1])), (int(r_points[0][2]),int(r_points[0][3])), (255,0,0), 5)
    else:
        img = origin_img
    
    cv2.imshow(title, img)

cv2.namedWindow(title)

model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

img_url = '/home/pi/Pictures/mycat.jpg'             # 0번 카메라 장치 연결 
origin_img = cv2.imread(img_url)
img = cv2.imread(img_url)

r = model(img_url)
r_points = r.pandas().xyxy[0].to_numpy()

cv2.createTrackbar('conf', title, 0, 100, nothing)
nothing(40)

#cv2.waitKey()
cv2.destroyAllWindows()
