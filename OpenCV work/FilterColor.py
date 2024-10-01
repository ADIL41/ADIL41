import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Open the default webcam

while True:
    ret, frame = cap.read()  # Read a frame from the webcam

    if not ret:  # Check if frame reading was successful
        print("Error: Unable to read frame from camera")
        break

    # Convert BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold of blue in HSV space (adjust values as needed)
    lower_blue = np.array([20, 150, 0])  # Experiment with these values for better detection
    upper_blue = np.array([220,255,255])

    # Create the mask for blue color detection
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply bitwise AND operation to get the blue color region
    # Ensure `mask` and `frame` have the same dimensions and data type (e.g., uint8)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, mask, and result
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    # Wait for a key press (0 for any key)
    if cv2.waitKey(1) == ord('q'):  # Exit on 'q' key press
        break

# Release resources
cap.release()
cv2.destroyAllWindows()