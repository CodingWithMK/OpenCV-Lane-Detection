import cv2
import numpy as np

video = cv2.VideoCapture("Driving on Road.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        video = cv2.VideoCapture("Driving on Road.mp4")
        continue

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_yellow = np.array([18, 175, 140])
    up_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    edges = cv2.Canny(mask, 75, 150)
    median = cv2.medianBlur(mask, 15)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)



    cv2.imshow("frame", frame)
    cv2.imshow("Edges", edges)
    cv2.imshow("Median", median)

    key = cv2.waitKey(25)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()