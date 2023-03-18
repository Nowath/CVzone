import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon = 0.8, maxHands = 2)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    hands,frame = detector.findHands(frame,flipType=False)
    
    if (hands):
        hand1 = hands[0]
        landmark1 = hand1["lmList"][4]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"] 
        handtype1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)
        #print('Hand 1',fingers1)
        #print(bbox1)
        
        if (len(hands)) == 2 :
            hand2 = hands[1]
            landmark2 = hand2["lmList"][8]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2["center"] 
            handtype2 = hand2["type"]
            fingers2 = detector.fingersUp(hand2)
            #print('Hand 2',fingers2)
            
            lenght,info,frame = detector.findDistance(landmark1,landmark2,frame)
            
    cv2.imshow("Hand Detector",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()