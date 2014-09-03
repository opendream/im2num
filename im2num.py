import cv2
import numpy as np

origin = cv2.imread('test.jpg', 0)
result = cv2.equalizeHist(origin)


preview = np.hstack((origin, result))

cv2.namedWindow( 'Display window', cv2.CV_WINDOW_AUTOSIZE );
cv2.imshow('Display window', preview)
cv2.waitKey(0)
cv2.destroyAllWindows()