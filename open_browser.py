from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pt
import pytesseract
import time
from rt_text_clicker import RT_TextClicker

rttc = RT_TextClicker(0.0001, 1)
button_region = (0, 0, 2560, 1600)


def click_textdata(target_text, region=None, interval=1, max_attempts=10):
    scaling_factor = 1
    screen = pt.screenshot(region=region)
    text_data = pytesseract.image_to_data(screen)
    for count, data in enumerate(text_data.splitlines()):
        if count > 0:
            data = data.split()
            if len(data) == 12 and target_text in data[11]:
                x, y, w, h = [int(num) / scaling_factor for num in data[6:10]]
                click_x, click_y = x + w / 2, y + h / 2
                print(f"Adjusted click position: ({click_x}, {click_y})")
                pt.click(click_x, click_y)
                break


def open_firefox(url):
    options = Options()
    options.add_argument("--zoom=1.2")  # Set zoom level (if needed)
    options.add_argument("--start-maximized")  # Maximizes but can sometimes not be true fullscreen
    # options.add_argument("--kiosk")  # True fullscreen mode
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    time.sleep(2)

    rttc.click_textdata("OK")

    driver.maximize_window()

    time.sleep(5)

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//strong[contains(text(), 'connect')"))
        )
        driver.find_element(By.XPATH, "//strong[contains(text(), 'connect')")

        print("Selenium")

    except Exception as e:
        print("Textclicker")

        rttc.click_textdata("connect")
        print(f"Navigation error: {e}")

    try:
        dropdown_trigger = driver.find_element(By.CSS_SELECTOR, "a[data-target='hardkeys_mfl_dropdown']")
        dropdown_trigger.click()  # Open the dropdown

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "HOME_1_BUTTON"))
        )

        home_button = driver.find_element(By.ID, "HOME_1_BUTTON")
        home_button.click()

        print("Selenium")

    except Exception as e:

        print(f"Navigation error: {e}")

    # click_textdata("AGREE")


def open_chrome(url):
    options = Options()
    options.add_argument("--zoom=1.2")  # Set zoom level (if needed)
    options.add_argument("--start-maximized")  # Maximizes but can sometimes not be true fullscreen
    # options.add_argument("--kiosk")  # True fullscreen mode
    import os
    os.environ["PATH"] = 'C:/Users/TimPfeiffer/Downloads/chromedriver_win32/chromedriver' + ";" + os.environ["PATH"]

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)

    rttc.click_textdata("OK")

    time.sleep(5)

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//strong[contains(text(), 'connect')"))
        )
        driver.find_element(By.XPATH, "//strong[contains(text(), 'connect')")

        print("Selenium")

    except Exception as e:
        print("Textclicker")

        rttc.click_textdata("connect")
        print(f"Navigation error: {e}")

    try:
        dropdown_trigger = driver.find_element(By.CSS_SELECTOR, "a[data-target='hardkeys_mfl_dropdown']")
        dropdown_trigger.click()  # Open the dropdown

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "HOME_1_BUTTON"))
        )

        home_button = driver.find_element(By.ID, "HOME_1_BUTTON")
        home_button.click()

        print("Selenium")

    except Exception as e:

        print(f"Navigation error: {e}")


if __name__ == "__main__":
    url = "https://mib-certs-target.joomo.de/ui/"
    # url = "https://fbref.com/en/"
    open_firefox(url)
