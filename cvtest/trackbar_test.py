import cv2

title = "track"
img1 = cv2.imread('tra.png')

def nothing(val):
    th = 255 - val
    canny_img = cv2.Canny(img1, th, th)
    cv2.imshow(title, canny_img)


cv2.namedWindow(title)

cv2.createTrackbar('name1', title, 0, 255, nothing)

nothing(0)

cv2.waitKey()