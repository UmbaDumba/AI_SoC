import cv2

s1 = cv2.imread('photo2.jpg')   #객체
s2 = cv2.imread('photo1.jpg')   #배경

diff = cv2.absdiff(s1, s2)
_, thre = cv2.threshold(diff, 120, 255, cv2.THRESH_BINARY)

cann = cv2.Canny(diff, 100, 200)

gray = cv2.cvtColor(thre, cv2.COLOR_BGR2GRAY)
contours, r = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_img = s2.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

cv2.imshow("diff", diff)
cv2.imshow("Threshold", thre)

cv2.imshow("Contours", contour_img)

cv2.waitKey()
cv2.destroyAllWindows()