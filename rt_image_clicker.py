import pyautogui as pt
from time import sleep
import cv2
from PIL import Image, ImageGrab
import imagehash

"""python --version
# API
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


class Test:pip
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
        position = pt.locateCenterOnScreen(target_png, confidence=0.5)
        print(f"Image found at position: {position}")
        pt.moveTo(position, duration=0.001)


    # navigation and clicking
    def click_image(self, target_png):
        position = pt.locateCenterOnScreen(target_png, confidence=0.7)
        print(f"Image found at position: {position}")
        pt.moveTo(position, duration=0.001)
        pt.leftClick()
