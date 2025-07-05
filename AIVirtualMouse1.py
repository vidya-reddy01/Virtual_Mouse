import cv2
import numpy as np
import HandTrackingModula2 as htm
import time
import autopy

###########################
wCam, hCam =640,432
#wCam, hCam =1000,1400
frameR = 100 #Frame Reduction
smoothening = 7
##########################
pTime=0
plocX,plocY = 0,0
clocX, clocY = 0,0

cap = cv2.VideoCapture(0)
cap.set(10,wCam)
cap.set(10,hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
#print(wScr, hScr)
while True:
    #1. Find the hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList)!=0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]


        #print(x1,y1,x2,y2)

    #2. Get the tip of the index and middle fingers


    #3. Check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)
        #4. Only Index finger : Moving mode
        if fingers[1]==1 and fingers[2]==0:

            #5. Convert Coordinates

            x3 = np.interp(x1,(frameR,wCam-frameR), (0, wScr))
            y3 = np.interp(y1,(frameR, hCam-frameR), (0, hScr))

            #6. Smoothen values
            clocX = plocX + (x3 - plocX)/smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            #7. Move Mouse
            autopy.mouse.move(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocX,plocY = clocX, clocY

        #8. Check if we are in clicking mode: Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8,12, img)
            print(length)
            # 10. Click Mouse if distance short
            if length < 35:
                cv2.circle(img,(lineInfo[4],lineInfo[5])
                           ,15,(0,255,0),cv2.FILLED)
                autopy.mouse.click()
                #autopy.mouse.click(autopy.mouse.Button.LEFT, delay=1)


        # if fingers[1] == 1 and fingers[0] == 1:
        #     # 9. Find distance between fingers
        #     length, img, lineInfo = detector.findDistance(8,12, img)
        #     print(length)
        #     # 10. Click Mouse if distance short
        #     if length < 40:
        #         cv2.circle(img,(lineInfo[4],lineInfo[5])
        #                    ,15,(0,255,0),cv2.FILLED)
        #         autopy.mouse.Button=RIGHT







    #11. Frame Rate
    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(30,50),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,0),3)
    #12. Display
    cv2.imshow("Image",img)
    cv2.waitKey(1)
