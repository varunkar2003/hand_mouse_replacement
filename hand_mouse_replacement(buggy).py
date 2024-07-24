import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Initialize MediaPipe components
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands

# Open the front camera
cap = cv2.VideoCapture(0)

# Set frame size for faster processing
frame_width = 640
frame_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

# Initialize hand tracking
hands = mphands.Hands()

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

prev_x, prev_y = 0, 0
prev_time = time.time()  # Initialize prev_time
click_threshold = 40  # Adjust distance threshold for click detection

while True:
    current_time = time.time()
    if current_time - prev_time > 1./30:  # Process at 30 FPS
        prev_time = current_time
        
        # Capture image from camera
        data, image = cap.read()
        if not data:
            break

        # Flip and convert image
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Hand detection
        results = hands.process(image_rgb)

        # Draw landmarks and handle mouse control
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(image, hand_landmarks, mphands.HAND_CONNECTIONS)

                # Get landmark positions
                landmarks = hand_landmarks.landmark

                # Map to screen coordinates
                screen_width, screen_height = pyautogui.size()
                x_index = int(landmarks[mphands.HandLandmark.INDEX_FINGER_TIP].x * screen_width)
                y_index = int(landmarks[mphands.HandLandmark.INDEX_FINGER_TIP].y * screen_height)
                x_thumb = int(landmarks[mphands.HandLandmark.THUMB_TIP].x * screen_width)
                y_thumb = int(landmarks[mphands.HandLandmark.THUMB_TIP].y * screen_height)

                # Smooth movement
                x_index = int((prev_x + x_index) / 2)
                y_index = int((prev_y + y_index) / 2)
                pyautogui.moveTo(x_index, y_index)
                prev_x, prev_y = x_index, y_index

                # Check for clicks
                distance = calculate_distance((x_index, y_index), (x_thumb, y_thumb))
                if distance < click_threshold:  # Adjust threshold as needed
                    pyautogui.click()
                    print(f"Click triggered! Distance: {distance}")

        # Show the image
        cv2.imshow('Handtracker', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
