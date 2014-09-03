import cv2
import numpy as np

origin = cv2.imread('test.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

result = cv2.equalizeHist(origin)

thresh = 127
result = cv2.threshold(result, thresh, 255, cv2.THRESH_BINARY)[1]

result = cv2.medianBlur(result, 3)

contours, hierarchy = cv2.findContours(result, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
idx =0
for cnt in contours:
    idx += 1
    x, y, w, h = cv2.boundingRect(cnt)
    roi = result[y:y+h, x:x+w]
    #cv2.imwrite(str(idx) + '.jpg', roi)
    cv2.rectangle(result, (x, y), (x+w, y+h), (200, 0, 0), 2)


preview = np.hstack((origin, result))
cv2.namedWindow( 'Display window', cv2.CV_WINDOW_AUTOSIZE );
cv2.imshow('Display window', preview)
cv2.waitKey(0)
cv2.destroyAllWindows()