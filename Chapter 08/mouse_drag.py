import pyautogui
import os

pyautogui.moveTo(800, 800)

# To open any program by their name recognized by windows or their path
os.startfile("mspaint")

distance = 400
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)  # move right
    distance -= 15
    pyautogui.drag(0, distance, duration=0.5)  # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 15
    pyautogui.drag(0, -distance, duration=0.5)  # move up
