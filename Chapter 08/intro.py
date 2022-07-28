import pyautogui

# mouse location coordinates x and y
print(pyautogui.position())

# screen resolution width and height
print(pyautogui.size())

# True if location coordinates x and y are within the screen
print(pyautogui.onScreen(1, 1))
