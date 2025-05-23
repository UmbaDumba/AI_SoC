import cv2
import subprocess

cap = cv2.VideoCapture(0)  # /dev/video0

gst_cmd = (
    "gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw,width=640,height=480,framerate=30/1 ! videoconvert ! jpegenc ! rtpjpegpay ! udpsink host=10.10.16.123 port=5000"
)

process = subprocess.Popen(gst_cmd, shell=True, stdin=subprocess.PIPE)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    process.stdin.write(frame.tobytes())