from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import scrapy
import pyautogui as pt
import pytesseract
import time


def screen_to_text(region=None):
    screen = pt.screenshot(region=region)
    text = pytesseract.image_to_data(screen)
    return text

def click_textdata(target_text, region=None, interval=1, max_attempts=10):
    scaling_factor=2
    text_data = screen_to_text(region)
    for count, data in enumerate(text_data.splitlines()):
        if count > 0:
            data = data.split()
            if len(data) == 12 and target_text in data[11]:
                x, y, w, h = [int(num) / scaling_factor for num in data[6:10]]
                click_x, click_y = x + w / 2, y + h / 2
                print(f"Adjusted click position: ({click_x}, {click_y})")
                pt.click(click_x, click_y)
                break

def open_website(url):
    options = Options()
    options.add_argument("--zoom=1.2")  # Set zoom level (if needed)
    options.add_argument("--start-maximized")  # Maximizes but can sometimes not be true fullscreen
    #options.add_argument("--kiosk")  # True fullscreen mode
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1)
    try:
        click_textdata(target_text="AGREE")

    except Exception as e:
        print(f"Error: {e}")

    # Deliberate delay to observe (Adjust as needed)
    time.sleep(2)

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "header_clubs"))
        )
        driver.find_element(By.ID, "header_clubs").click()
        print("Clicked header_clubs")
    except Exception as e:
        print(f"Navigation error at header_clubs: {e}")

        time.sleep(3)
    try:
        # Wait for submenu to potentially load
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="div_popular_clubs_m"]/div/a[3]'))
        )
        driver.find_element(By.XPATH, '//*[@id="div_popular_clubs_m"]/div/a[3]').click()

        print("Clicked Club")

    except Exception as e:
        print(f"Navigation error at club: {e}")


if __name__ == "__main__":
    url = "https://fbref.com/en/"
    open_website(url)

