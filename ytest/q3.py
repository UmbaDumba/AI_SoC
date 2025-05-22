
import torch
import cv2

title = "yolo_result"


model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s


cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결 

# 코덱 정의
#fourcc = cv2.VideoWrite_fourcc('D','I','V','X')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 위와 같은 결과

# 프레임 크기, FPS 정의
width  = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#fps = cap.get(cv2.CAP_PROP_FPS)  # 영상 속도
#fps = cap.get(cv2.CAP_PROP_FPS) * 2  # 영상 재생속도 2배
fps = 30

out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
# 파일 저장명, 코덱, FPS, 크기(width, height)

is_record = False

if cap.isOpened():                      # 캡쳐 객체 연결 확인
    while True:
        if cv2.waitKey(1) == ord('q'):
            out.release()
            break   
        
        ret, frame = cap.read()           # 다음 프레임 읽기
        if ret:

            if is_record == False:
                r = model(frame)
                r_points = r.pandas().xyxy[0].to_numpy()
                for p in r_points:
                    if p[6] == 'person':
                        is_record = True
            
            cv2.imshow(title, frame)

            if is_record:
                out.write(frame)  
        else:
            print('no frame')
            break
else:
    print("can't open camera.")


cap.release()
cv2.destroyAllWindows()