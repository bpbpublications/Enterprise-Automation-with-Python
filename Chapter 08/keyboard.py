import pyautogui
import os

# Minimize mu application
pyautogui.getWindowsWithTitle("keyboard.py")[0].minimize()
# type with 0.05 second pause in between each key
pyautogui.write('I am automation bot', interval=0.05)
# Press the hotkey combinations.
pyautogui.hotkey('ctrl', 'a', interval=0.05)
pyautogui.hotkey('ctrl', 'c', interval=0.05)
pyautogui.hotkey('ctrl', 'v', interval=0.05)
pyautogui.hotkey('ctrl', 'v', interval=0.05)

# Make an alert box appear and pause the program until OK is clicked.
pyautogui.alert('Completed the automation.')
