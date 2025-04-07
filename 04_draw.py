import cv2
import numpy as np

cap = cv2.VideoCapture("./resources/downloads/test_video.mp4")

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (120, 120, 120), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "Hello", (200, height -10), font, 4, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow("frame", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
