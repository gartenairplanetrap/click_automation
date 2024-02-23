import pyautogui as pt
from time import sleep
import cv2
from PIL import Image, ImageGrab
import imagehash


class Comparer:

    def __init__(self):
        pt.FAILSAFE = True

    def compare(self, file, name):
        # loading images
        image = cv2.imread(file)
        screenshot_filepath = f"C:/Users/TimPfeiffer/Pictures/Screenshots/{name}Screenshot.png"
        screenshot = pt.screenshot(screenshot_filepath, region=(250, 400, 1200, 600))
        screenshot = cv2.imread(screenshot_filepath)

        im1 = Image.open(file)
        im2 = Image.open(screenshot_filepath)

        # hashing for mathematical comparison
        hash1 = imagehash.average_hash(im1)
        hash2 = imagehash.average_hash(im2)

        hamming_distance = hash1 - hash2

        # print(f"Hamming distance is: {hamming_distance}")

        # sim = 100.0 - (hamming_distance / len(hash2.hash) * 100.0)

        sim = 100 - (2*hamming_distance)

        are_sim = sim >= 70.0

        # visual representation of difference
        im1cv = cv2.imread(file)
        im2cv = cv2.imread(screenshot_filepath)

        difference = cv2.absdiff(im1cv, im2cv)

        # output Pass/Fail
        if are_sim:
            cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}_Differences.png", difference)
            print(f"{name} Images are the same")
            print(f"Sim is: {sim}")
            return sim
        else:
            cv2.imwrite(f"C:/Users/TimPfeiffer/Pictures/{name}_Differences.png", difference)
            print(f"{name} Images not the same")
            print(f"Sim is: {sim}")
            cv2.imshow("Difference", difference)
            return sim

    """
    # compare for Radio
    def compare_radio(self, file1, file2, file3, name):
        image1 = cv2.imread(file1)
        image2 = cv2.imread(file2)
        image3 = cv2.imread(file3)
        screenshot_filepath = f"C:/Users/TimPfeiffer/Pictures/Screenshots/{name}Screenshot.png"
        screenshot = pt.screenshot(screenshot_filepath, region=(250, 400, 1200, 600))
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
                """
