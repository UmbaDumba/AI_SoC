
import torch
import cv2

def nothing(val):
    th = 255 - val
    canny_img = cv2.Canny(img1, th, th)
    cv2.imshow(title, canny_img)



model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결 

if cap.isOpened():                      # 캡쳐 객체 연결 확인
    while True:
        if cv2.waitKey(1) == ord('q'):
                break   
        
        ret, frame = cap.read()           # 다음 프레임 읽기
        if ret:
            r = model(frame)
            r.show()
            
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
            
cap.release()
cv2.destroyAllWindows()
# cv2.destroyWindow(winname)으로 특정 윈도우 창만