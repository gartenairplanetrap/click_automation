import pyautogui as pt
import pytesseract
from PIL import Image, ImageOps, ImageFilter
from time import sleep
import numpy as np
import cv2

# pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class RT_TextClicker:
    def __init__(self, speed, scaling_factor=1):
        self.speed = speed
        self.scaling_factor = scaling_factor
        pt.FAILSAFE = True

    def click_textdata(self, target_text, region=None, interval=1, max_attempts=10, confidence_threshold=50):
        screen = pt.screenshot(region=region)
        # Convert PIL Image to NumPy array
        screen_np = np.array(screen)
        screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)  # Convert from RGB (PIL) to BGR (OpenCV)

        # Convert to YUV color space and apply histogram equalization to the Y channel (luminance)
        yuv = cv2.cvtColor(screen_np, cv2.COLOR_BGR2YUV)
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])

        # Convert back to BGR color space
        result = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        binary_image = cv2.threshold(result_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        text_data = pytesseract.image_to_data(binary_image, output_type=pytesseract.Output.DICT)

        clicked = False
        for i, text in enumerate(text_data['text']):
            if target_text in text and int(text_data['conf'][i]) >= confidence_threshold:
                x, y, w, h = [int(num) / self.scaling_factor for num in
                              [text_data['left'][i], text_data['top'][i], text_data['width'][i],
                               text_data['height'][i]]]
                pos_x, pos_y = x + w / 2, y + h / 2
                print(f"Text ({target_text}) found at position: ({pos_x}, {pos_y})")
                # print(f"Confidence: {int(text_data['conf'][i])}")
                pt.click(pos_x, pos_y)
                clicked = True
                return 1

        if not clicked:
            print(f"Error: Text '{target_text}' not found or confidence level below threshold.")
            return 0

    def hover_textdata(self, target_text, region=None, interval=1, max_attempts=10, confidence_threshold=60):
        screen = pt.screenshot(region=region)
        # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        text_data = pytesseract.image_to_data(screen, output_type=pytesseract.Output.DICT)
        hovered = False
        for i, text in enumerate(text_data['text']):
            if target_text in text and int(text_data['conf'][i]) >= confidence_threshold:
                x, y, w, h = [int(num) / self.scaling_factor for num in
                              [text_data['left'][i], text_data['top'][i], text_data['width'][i],
                               text_data['height'][i]]]
                pos_x, pos_y = x + w / 2, y + h / 2
                print(f"Text ({target_text}) found at position: ({pos_x}, {pos_y})")
                pt.moveTo(pos_x, pos_y)
                hovered = True
                return 1

        if not hovered:
            print(f"Error: Text '{target_text}' not found or confidence level below threshold.")
            return 0

    def click_textbutton(self, target_text, region=None, interval=1, max_attempts=10, confidence_threshold=50):
        screen = pt.screenshot(region=region)
        # Convert PIL Image to NumPy array
        screen_np = np.array(screen)
        screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)  # Convert from RGB (PIL) to BGR (OpenCV)

        # Convert to YUV color space and apply histogram equalization to the Y channel (luminance)
        yuv = cv2.cvtColor(screen_np, cv2.COLOR_BGR2YUV)
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])

        # Convert back to BGR color space
        result = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        binary_image = cv2.threshold(result_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        text_data = pytesseract.image_to_data(binary_image, output_type=pytesseract.Output.DICT)

        offset_pixels = 40
        clicked = False
        for i, text in enumerate(text_data['text']):
            if target_text in text and int(text_data['conf'][i]) >= confidence_threshold:
                x, y, w, h = [int(num) / self.scaling_factor for num in
                              [text_data['left'][i], text_data['top'][i], text_data['width'][i],
                               text_data['height'][i]]]
                pos_x, pos_y = x + w / 2, y + h / 2 + offset_pixels  # Added offset to y-coordinate
                print(f"Text ({target_text}) found at adjusted position: ({pos_x}, {pos_y})")
                pt.click(pos_x, pos_y)
                clicked = True
                return 1

        if not clicked:
            print(f"Error: Text '{target_text}' not found or confidence level below threshold.")
            return 0
