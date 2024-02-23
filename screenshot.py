import pyautogui as pt
from time import sleep
import cv2

sleep(4)

screenshot_filepath = f"C:/Users/TimPfeiffer/Pictures/Screens/RT_Settings_Screen.png"
screenshot = pt.screenshot(screenshot_filepath, region=(250, 400, 1200, 600))
screenshot = cv2.imread(screenshot_filepath)
