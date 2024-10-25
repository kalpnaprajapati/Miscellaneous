import cv2
import numpy as np
import pyautogui

# Screen resolution
SCREEN_SIZE = tuple(pyautogui.size())

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("outputvideo.mp4", fourcc, 20.0, (SCREEN_SIZE))

# Record duration in seconds
record_seconds = 30

for _ in range(int(record_seconds * 20)):
    # Capture the screen
    img = pyautogui.screenshot()
    
    # Convert the image to a numpy array
    frame = np.array(img)
    
    # Convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Write the frame
    out.write(frame)
    
    # Display the frame (optional)
    cv2.imshow("Screen Recorder", frame)
    
    # Exit recording if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the VideoWriter and close windows
out.release()
cv2.destroyAllWindows()