import numpy as np
import cv2 as cv
cap = cv.VideoCapture('IMG_2422.MOV')

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20,0, (480, 640))
print(fourcc)
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out_frame = cv.resize(gray, (480, 640))
    cv.rectangle(out_frame,(384,0),(510,128), 0, 10 )
    out.write(out_frame) 
    cv.imshow('frame', out_frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
out.release()
cv.destroyAllWindows()