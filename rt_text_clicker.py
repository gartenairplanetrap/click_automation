import pyautogui as pt
import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

class RT_TextClicker:
    def __init__(self, speed):
        self.speed = speed
        pt.FAILSAFE = True

    # Capture the screen and extract text from it
    def screen_to_text(self, region=None):
        screen = pt.screenshot(region=region)
        text = pytesseract.image_to_string(screen)
        return text

    # Check for the presence of the specified text within a screen region
    def nav_to_text(self, target_text, region=None):
        screen_text = self.screen_to_text(region)
        return target_text in screen_text

    # Click at the center of the provided region
    def click_text(self, target_text, region=None, interval=1, max_attempts=10):
        if self.nav_to_text(target_text, region):
            x, y = region[0] + region[2] / 2, region[1] + region[3] / 2
            pt.click(x, y)

# Example usage
if __name__ == "__main__":
    rttc = RT_TextClicker(speed=0.001)
    button_region = (300, 300, 100, 50)
    rttc.click_text("Radio", button_region)