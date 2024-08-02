# handdetection-canva
using media pipe that already has already been trained on various hand images to have different and have hand landmarks we will detect the hand and make the computer screen accessible using our hand.

The MediaPipe Hands module identifies 21 key landmarks on each hand. These landmarks correspond to specific points on the hand, such as finger joints and the wrist. Here's a list of the 21 hand landmarks and their corresponding locations:

WRIST: The base of the palm.
THUMB_CMC: The Carpometacarpal (CMC) joint of the thumb.

THUMB_MCP: The Metacarpophalangeal (MCP) joint of the thumb.

THUMB_IP: The Interphalangeal (IP) joint of the thumb.

THUMB_TIP: The tip of the thumb.

INDEX_FINGER_MCP: The Metacarpophalangeal (MCP) joint of the index finger.

INDEX_FINGER_PIP: The Proximal Interphalangeal (PIP) joint of the index finger.

INDEX_FINGER_DIP: The Distal Interphalangeal (DIP) joint of the index finger.

INDEX_FINGER_TIP: The tip of the index finger.

MIDDLE_FINGER_MCP: The Metacarpophalangeal (MCP) joint of the middle finger.

MIDDLE_FINGER_PIP: The Proximal Interphalangeal (PIP) joint of the middle finger.

MIDDLE_FINGER_DIP: The Distal Interphalangeal (DIP) joint of the middle finger.

MIDDLE_FINGER_TIP: The tip of the middle finger.

RING_FINGER_MCP: The Metacarpophalangeal (MCP) joint of the ring finger.

RING_FINGER_PIP: The Proximal Interphalangeal (PIP) joint of the ring finger.

RING_FINGER_DIP: The Distal Interphalangeal (DIP) joint of the ring finger.

RING_FINGER_TIP: The tip of the ring finger.

PINKY_MCP: The Metacarpophalangeal (MCP) joint of the pinky finger.

PINKY_PIP: The Proximal Interphalangeal (PIP) joint of the pinky finger.

PINKY_DIP: The Distal Interphalangeal (DIP) joint of the pinky finger.

PINKY_TIP: The tip of the pinky finger



we can call these in built hand landmarks and make our finger nodes accesible

this is the image data of how these landmarks look connected

![image](https://github.com/user-attachments/assets/c33c0770-f00b-421d-8c22-5559fc4e79af)



we then import pyautogui which has all the mouse functions in it we can write code to replace the mouse functions with our hand landmarks mapped out mediapipe

