import pyautogui as pt
import pytesseract
from PIL import Image
from time import sleep

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class RT_TextClicker:
    def __init__(self, speed, scaling_factor=1):
        self.speed = speed
        self.scaling_factor = scaling_factor
        pt.FAILSAFE = True


    # Capture the screen and extract text from it
    def screen_to_text(self, region=None):
        screen = pt.screenshot(region=region)
        text = pytesseract.image_to_data(screen)
        return text

    # Check for the presence of the specified text within a screen region
    def nav_to_text(self, target_text, region=None):
        screen_text = self.screen_to_text(region)
        return target_text in screen_text

    # Click at the center of the provided region
    def click_text(self, target_text, region=None, interval=1, max_attempts=10):
        if self.nav_to_text(target_text, region):
            x, y = region[0] + region[2] / 2, region[1] + region[3] / 2
            print(x, y)
            pt.click(x, y)

    def click_textdata(self, target_text, region=None, interval=1, max_attempts=10):
        text_data = self.screen_to_text(region)
        for count, data in enumerate(text_data.splitlines()):
            if count > 0:
                data = data.split()
                if len(data) == 12 and target_text in data[11]:
                    x, y, w, h = [int(num) / self.scaling_factor for num in data[6:10]]
                    click_x, click_y = x + w / 2, y + h / 2
                    print(f"Adjusted click position: ({click_x}, {click_y})")
                    pt.click(click_x, click_y)
                    break

# Example usage
if __name__ == "__main__":
    # scaling=2 was necessary for my own display. You may need to change/remove it
    rttc = RT_TextClicker(0.001, 2)
    sleep(2)
    button_region = (0, 0, 2560, 1600)
    rttc.click_textdata("Radio", button_region)
