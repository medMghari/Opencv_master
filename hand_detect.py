import cv2
import numpy as np


cap = cv2.VideoCapture(0)
ret,frame = cap.read()

# setup initial location of window
# r,h,c,w = 250,90,400,125  # simply hardcoded the values
r,h,c,w = 30,150,155,80  # simply hardcoded the values

track_window = (c,r,w,h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]

hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
cap.release()

#figure()

for index in range(3):
    
    cap = cv2.VideoCapture(0)

    while(True):
        ret ,frame = cap.read()

        if ret == True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

            # apply meanshift to get the new location
            ret, track_window = cv2.CamShift(dst, track_window, term_crit)

            # Draw it on image
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            img2 = cv2.polylines(frame,[pts],True, 255,2)
            cv2.imshow('img2',img2)
            #imshow(cv2.cvtColor(img2,4))
            #show()
            #clear_output(wait=True)


        else:
            break

    cap.release()