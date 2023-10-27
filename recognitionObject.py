import cv2
import numpy as np

frame = cv2.imread("test3.png", 1)

img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(img, 235,255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_SIMPLEX
for cnt in contours:
    if cv2.contourArea(cnt) > 1500:
        approx  = cv2.approxPolyDP(cnt, 0.01* cv2.arcLength(cnt, True), True)
        cv2.drawContours(frame, [approx], -1, (0,255,0), 2)
        # x = approx.ravel()[0]
        # y = approx.ravel()[1]

        # if len(approx) == 3:
        #     cv2.putText(frame, "Tam Giac", (x,y), font, 1, (0,0,255),  2, cv2.LINE_AA)
        # elif len(approx) == 4:
        #     cv2.putText(frame, "Chu Nhat", (x,y), font, 1, (0,0,255), 2, cv2.LINE_AA)
        # elif len(approx) == 5:
        #     cv2.putText(frame, "Ngu Giac", (x,y), font, 1, (0,0,255),  2, cv2.LINE_AA)
        # elif len(approx) == 6:
        #     cv2.putText(frame, "Luc Giac", (x,y), font, 1, (0,0,255), 2, cv2.LINE_AA)
        # else :
        #     cv2.putText(frame, "Hinh Tron", (x,y), font, 1, (0,0,255), 2, cv2.LINE_AA)

cv2.imshow("Hinh Dang", frame)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
