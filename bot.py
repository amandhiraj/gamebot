import mss
import numpy as np
import cv2
from PIL import Image

# Load Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize screen capture (capturing Firefox window based on its coordinates)
with mss.mss() as sct:
    monitor = sct.monitors[1]  # Capture the first monitor (adjust if needed)
    
    while True:
        # Capture the screen (adjust the monitor region for Firefox window capture)
        screenshot = sct.grab(monitor)
        
        # Convert the captured image to a numpy array
        img = np.array(screenshot)
        
        # Convert to BGR (OpenCV uses BGR format)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

        # Convert the image to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw bounding boxes around the detected faces and label them
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Display the live screen with detected faces
        cv2.imshow("Live Screen Capture with Face Detection", img)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean up
cv2.destroyAllWindows()
