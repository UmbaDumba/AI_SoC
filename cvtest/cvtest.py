import cv2

cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결 

if cap.isOpened():                      # 캡쳐 객체 연결 확인
    while True:
        ret, frame = cap.read()           # 다음 프레임 읽기
        if ret:
            cv2.imshow('camera', frame)   # 다음 프레임 이미지 표시
            if cv2.waitKey(1) == ord('q'):
                cv2.imwrite('photo1.jpg', frame) # 프레임을 'photo.jpg'에 저장
                break    
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
            
cap.release()
cv2.destroyAllWindows()
# cv2.destroyWindow(winname)으로 특정 윈도우 창만