import cv2

cap = cv2.VideoCapture(0)

# 코덱 정의
#fourcc = cv2.VideoWrite_fourcc('D','I','V','X')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 위와 같은 결과

# 프레임 크기, FPS 정의
width  = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)  # 영상 속도
#fps = cap.get(cv2.CAP_PROP_FPS) * 2  # 영상 재생속도 2배

out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
# 파일 저장명, 코덱, FPS, 크기(width, height)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    out.write(frame)  # 영상 데이터만 저장 (소리 없음)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

out.release()  # 자원 해제
cap.release()
cv2.destroyAllWindows()