import pyautogui

# Move the mouse to XY coordinates.
pyautogui.moveTo(1, 12)
# Click the mouse.
pyautogui.click()
# Double click the mouse.
pyautogui.doubleClick()

# Use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
