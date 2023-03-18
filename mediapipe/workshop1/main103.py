import cv2

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
text = 'Hello SnowMan!'
font = cv2.FONT_HERSHEY_SIMPLEX
color_font = (172,114,250)
font_sacle = 1

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.putText(frame,text,(105,123),font,font_sacle,color_font,thickness = 2)
    cv2.imshow('Video Capture',frame)
    print(fps)
    if(cv2.waitKey(1)) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()