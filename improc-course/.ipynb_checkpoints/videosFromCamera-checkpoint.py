# run this in a script

import cv2

cap = cv2.VideoCapture(0) # grab default camera

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# windows --> DIVX
# LINUX --> XVID

writer = cv2.VideoWriter('logs/videosFromCamera.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(width,height)) # read the docs

while True:
    ret,frame = cap.read() # returning single images everytime
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame',gray)
    ret, thresh1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)

    writer.write(thresh1)
    
    cv2.imshow('frame',thresh1)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release() # stop capturing
writer.release()
cv2.destroyAllWindows()