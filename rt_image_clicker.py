import pyautogui as pt
from time import sleep
import cv2
from PIL import Image
import imagehash

"""
# API
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


class Test:
    cases = []

    def __init__(self, testid):
        self.testid = testid

    @app.route("/get_test/<test_id>")
    def get_results(self):
        return jsonify(self.cases)

    def print_cases(self):
        for case in self.cases:
            print(case)

    def add_testcase(self, case):
        self.cases.append(case)


class Testcase(Test):
    def __init__(self, testid, caseid, name, result):
        super().__init__(testid)
        self.caseid = caseid
        self.name = name
        self.expexted_result = "Selectable"
        self.result = result
        self.add_testcase(self)

    def __repr__(self):
        return f"({self.caseid}. {self.name}: Expected({self.expexted_result}), Result({self.result}))"

    @app.route("/get_result/<case_id>")
    def get_result(self):
        api_endpoint = "http://endpoint/get_result"
        data = {
            "caseid": self.caseid,
            "name": self.name,
            "expected": self.expexted_result,
            "result": self.result
        }
        try:
            response = requests.post(api_endpoint,json=data)
            if response.status_code == 201:
                return jsonify(data)
            else:
                return jsonify(f"Sending of test result failed: {self.caseid}")
        except requests.RequestException as rex:
            return jsonify(f"API connection failed: {e}")

"""


class RT_ImageClicker:
    def __init__(self, speed):
        self.speed = speed  # speed of the mouse movement
        pt.FAILSAFE = True

    # without clicking for hovering over hardkeys
    def nav_to_image(self, target_png):
        try:
            position = pt.locateCenterOnScreen(target_png, confidence=0.8)  # x, y coordinates of located image
            pt.moveTo(position, duration=self.speed)
        except Exception as Image_not_found_exception:
            print(f'No image found: {Image_not_found_exception}')

    # navigation and clicking
    def click_image(self, target_png):
        try:
            position = pt.locateCenterOnScreen(target_png, confidence=0.8)  # x, y coordinates of located image
            pt.moveTo(position, duration=self.speed)
            pt.leftClick()
        except Exception as Image_not_found_exception:
            print(f'No image found: {Image_not_found_exception}')

    # compare for Media and Menu
    def compare(self, file, name):
        # loading images
        image = cv2.imread(file)
        screenshot_filepath = f"C:/Users/TimPfeiffer/Pictures/Screenshots/{name}Screenshot.png"
        screenshot = pt.screenshot(screenshot_filepath, region=(300, 350, 1300, 550))
        screenshot = cv2.imread(screenshot_filepath)

        im1 = Image.open(file)
        im2 = Image.open(screenshot_filepath)

        # hashing for mathematical comparison
        hash1 = imagehash.average_hash(im1)
        hash2 = imagehash.average_hash(im2)

        hamming_distance = hash1 - hash2

        print(f"Hamming distance is: {hamming_distance}")

        sim = 100.0 - (hamming_distance / len(hash2.hash) * 100.0)

        are_sim = sim >= 90.0

        # visual representation of difference
        im1cv = cv2.imread(file)
        im2cv = cv2.imread(screenshot_filepath)

        difference = cv2.absdiff(im1cv, im2cv)

        # output Pass/Fail
        if are_sim:
            cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}_Differences.png", difference)
            print(f"{name} Images are the same")
            print(f"Sim is: {sim}")
            return f"Pass: {sim}"
        else:
            cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}_Differences.png", difference)
            print(f"{name} Images not the same")
            print(f"Sim is: {sim}")
            cv2.imshow("Difference", difference)
            return f"Fail: {sim}"


    # compare for Radio
    def compare_radio(self, file1, file2, file3, name):
        image1 = cv2.imread(file1)
        image2 = cv2.imread(file2)
        image3 = cv2.imread(file3)
        screenshot_filepath = f"C:/Users/TimPfeiffer/Pictures/Screenshots/{name}Screenshot.png"
        screenshot = pt.screenshot(screenshot_filepath, region=(300, 450, 1300, 450))
        screenshot = cv2.imread(screenshot_filepath)

        im1 = Image.open(file1)
        im2 = Image.open(file2)
        im3 = Image.open(file3)
        imscreenshot = Image.open(screenshot_filepath)

        hash1 = imagehash.average_hash(im1)
        hash2 = imagehash.average_hash(im2)
        hash3 = imagehash.average_hash(im3)
        hashscreenshot = imagehash.average_hash(imscreenshot)

        hamming_distance1 = hash1 - hashscreenshot
        hamming_distance2 = hash2 - hashscreenshot
        hamming_distance3 = hash3 - hashscreenshot

        print(f"Hamming distance 1 is: {hamming_distance1}")
        print(f"Hamming distance 2 is: {hamming_distance2}")
        print(f"Hamming distance 3 is: {hamming_distance3}")

        sim1 = 100.0 - (hamming_distance1 / len(hash1.hash) * 100.0)
        sim2 = 100.0 - (hamming_distance2 / len(hash2.hash) * 100.0)
        sim3 = 100.0 - (hamming_distance3 / len(hash3.hash) * 100.0)

        are_sim1 = sim1 >= 80.0
        are_sim2 = sim2 >= 80.0
        are_sim3 = sim3 >= 80.0

        im1cv = cv2.imread(file1)
        im2cv = cv2.imread(file2)
        im3cv = cv2.imread(file3)
        imscreenshotcv = cv2.imread(screenshot_filepath)

        if sim1 >= sim2 and sim1 >= sim3:
            difference = cv2.absdiff(im1cv, imscreenshotcv)
            if are_sim1:
                cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}1_Differences.png", difference)
                print(f"{name} Images are the same")
                print(f"Sim1 is: {sim1}")
                return f"Pass: {sim1}"
            else:
                cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}1_Differences.png", difference)
                print(f"{name} Images not the same")
                print(f"Sim1 is: {sim1}")
                return f"Fail: {sim1}"

        elif sim2 >= sim1 and sim2 >= sim3:
            difference = cv2.absdiff(im2cv, imscreenshotcv)
            if are_sim2:
                cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}2_Differences.png", difference)
                print(f"{name} Images are the same")
                print(f"Sim2 is: {sim2}")
                return f"Pass: {sim2}"
            else:
                cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}2_Differences.png", difference)
                print(f"{name} Images not the same")
                print(f"Sim2 is: {sim2}")
                return f"Fail: {sim2}"

        else:
            difference = cv2.absdiff(im3cv, imscreenshotcv)
            if are_sim3:
                cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}3_Differences.png", difference)
                print(f"{name} Images are the same")
                print(f"Sim3 is: {sim3}")
                return f"Pass: {sim3}"
            else:
                cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}3_Differences.png", difference)
                print(f"{name} Images not the same")
                print(f"Sim3 is: {sim3}")
                return f"Fail: {sim3}"


if __name__ == "__main__":
    # test1 = Test(1)
    rtc = RT_ImageClicker(speed=0.001)

    sleep(3)

    rtc.nav_to_image("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Hardkeys.png")

    sleep(1)

    rtc.click_image("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Radio_Key.png")

    sleep(7)

    result_radio = rtc.compare_radio("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Radio_Screen1.png",
                                     "C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Radio_Screen2.png",
                                     "C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Radio_Screen3.png", "Radio")

    sleep(1)
    # radio_main_screen = Testcase(1, 1, "Radio Mainscreen", result_radio)

    rtc.nav_to_image("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Hardkeys.png")

    sleep(1)

    rtc.click_image("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Menu_Key.png")

    sleep(2)

    result_gridmenu = rtc.compare("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Gridmenu_Screen.png", "Gridmenu")

    sleep(1)
    # gridmenu = Testcase(1, 2, "Gridmenu", result_gridmenu)

    rtc.click_image("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Media_Button.png")

    sleep(2)

    rtc.click_image("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Media_TrDetails_Button.png")

    sleep(2)

    result_media = rtc.compare("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Media_Screen.png", "Media")

    sleep(1)
    # media_main_screen = Testcase(1, 3, "Media Track Details", result_media)

    rtc.click_image("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Media_Favorites_Button.png")

    sleep(3)

    result_media_fav = rtc.compare("C:/Users/TimPfeiffer/Pictures/Screenshots/RT_Media_Favorites_Screen.png",
                                   "Media_Favorites")

    sleep(1)
    # media_favorites = Testcase(1, 4, "Media Favorites", result_media_fav)

    # print(Test.cases)