import pyautogui

imageLocation = pyautogui.locateOnScreen('loadImage.png')

imagePoint = pyautogui.center(imageLocation)
print(imagePoint)

imageX, imageY = imagePoint
# clicks the center of where the image was found
pyautogui.click(imageX, imageY)
