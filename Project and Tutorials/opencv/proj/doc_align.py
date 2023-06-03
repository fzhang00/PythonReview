import cv2 as cv
import sys
import numpy as np

img_name = "IMG-2420.jpg"
old_points = []

def draw_circle(event, x, y, flags, param):
    global old_points
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img_vis,(x,y),25,(255,0,0),-1)
        old_points.append((x,y))
        print(x,y)

img = cv.imread(img_name,  cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")

img = cv.resize(img, None, fx = 0.5, fy = 0.5, interpolation= cv.INTER_LINEAR)
(rows, cols) = img.shape
new_points = [(0, 0), (0, rows), (cols, 0), (cols, rows)]
img_vis = img.copy()

cv.namedWindow('Display window')
cv.setMouseCallback('Display window', draw_circle)
while(1):
    if len(old_points) == 4:
        M = cv.getPerspectiveTransform(np.float32(old_points), np.float32(new_points))
        dst = cv.warpPerspective(img,M,(cols,rows))
    else:
        # print(old_points)
        dst = img
    cv.imshow("Display window", img_vis)
    cv.imshow("Aligned image", dst)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv.imwrite(img_name.split(".")[0]+"_aligned.png", dst)