# 🖱️ Virtual Mouse Using Hand Gestures (OpenCV + MediaPipe)
This project implements a virtual mouse system that allows users to control the mouse pointer using hand gestures. Using a standard webcam, it captures hand movements in real-time and translates them into mouse actions such as moving the cursor and clicking — offering a contactless interface experience.

🛠 Technologies Used:    
  * Python  
  * OpenCV – for capturing video frames and image processing    
  * MediaPipe Hands – for hand detection and landmark tracking  
  * PyAutoGUI – for mouse movement and click automation  

🔁 Workflow Overview -- The system architecture includes the following key steps:  
  * Video Capture: Webcam feed is captured via OpenCV.  
  * Hand Detection: MediaPipe identifies hand and 21 landmarks.  
  * Gesture Recognition: Logic determines which fingers are up and calculates finger positions.  
  * Mouse Control: PyAutoGUI is used to control cursor and clicks.  

✋ Supported Gestures -- Gesture	Description	Action:  
  * Index Finger Up	---> Only index finger raised	---> Move mouse cursor  
  * Index + Middle Up	---> Both fingers raised closely	---> Left click (pinch gesture)  
