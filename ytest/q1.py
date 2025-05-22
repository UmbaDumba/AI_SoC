import torch
import cv2

title = "yolo_result"

def nothing(val):
    # val : confidence * 100
    conf = val / 100.0
    print(conf)
    img = cv2.imread(img_url)
    for p in r_points:
        if p[4] > conf:
            img = cv2.rectangle(img, (int(p[0]),int(p[1])), (int(p[2]),int(p[3])), (255,0,0), 5)
        else:
            pass
    
    cv2.imshow(title, img)


model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

img_url = '/home/pi/Pictures/mycat.jpg'             # 0번 카메라 장치 연결 
origin_img = cv2.imread(img_url)
img = cv2.imread(img_url)

r = model(img_url)
r_points = r.pandas().xyxy[0].to_numpy()

# print("test----------------")
# print(type(r_points[0][4]))
# print(r_points[0][4])

cv2.imshow('origin_imgae', origin_img)
cv2.namedWindow(title)
cv2.createTrackbar('conf', title, 0, 100, nothing)
nothing(40)

cv2.waitKey()
cv2.destroyAllWindows()
