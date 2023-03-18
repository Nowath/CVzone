import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(1)
detecter = FaceDetector()
text = 'Natheepat'
font = cv2.FONT_HERSHEY_TRIPLEX
text_color = (172,114,250)
fps = cv2.CAP_PROP_FPS

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    frame,bbox = detecter.findFaces(frame)
    cv2.putText(frame,text,(0,60),font,1,text_color,thickness = 2)
    if bbox:
        center = bbox[0]["center"]
    print(fps)
    cv2.imshow("Face Detector",frame)
    
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()