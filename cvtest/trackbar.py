import cv2

def nothing():
    pass

title = 'Trackbar test'

cv2.namedWindow(title)

#Canny threshold용 트랙바 2개 생성,
cv2.createTrackbar('Min Threshold', title, 50, 255, nothing)
cv2.createTrackbar('Max Threshold', title, 150, 255, nothing)

#웹캠 연결,
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 트랙바 값 읽기
    min_val = cv2.getTrackbarPos('Min Threshold', title)
    max_val = cv2.getTrackbarPos('Max Threshold', title)

    # Canny 엣지 검출
    edges = cv2.Canny(gray, min_val, max_val)

    # 결과 표시
    cv2.imshow(title, edges)

    if cv2.waitKey(1) == 27:  # ESC 키 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()