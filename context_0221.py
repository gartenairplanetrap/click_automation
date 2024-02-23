from rt_image_clicker import RT_ImageClicker
from rt_text_clicker import RT_TextClicker
from comparer import Comparer
import pyautogui as pt
from time import sleep

rttc = RT_TextClicker(0.0001, 1)
rtic = RT_ImageClicker(0.001)
comp = Comparer()
button_region = (0, 0, 2560, 1600)

context_status = {}


def phone():
    print("\nContext: Phone")
    retry_count = 0
    while retry_count < 3:
        try:
            rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Target0221/Buttons/Grid.png")

            sleep(1)

            rttc.click_textdata("Telefon", button_region)

            break

        except Exception as e:
            retry_count += 1
            print(f"Error {e}")


def grid():
    print("\nContext: Grid")
    retry_count = 0
    while retry_count < 3:
        try:
            rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Target0221/Buttons/Grid.png")

            sleep(1)

            break

        except Exception as e:
            retry_count += 1
            print(f"Error {e}")


def radio_media():
    print("\nContext: Radio, Media")
    retry_count = 0
    while retry_count < 3:
        try:
            rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Target0221/Buttons/Grid.png")

            sleep(1)

            rttc.click_textdata("Radio", button_region)

            break

        except Exception as e:
            retry_count += 1
            print(f"Error {e}")




def navi():
    return 1


def sound():
    return 1


def settings():
    return 1


def vehicle():
    return 1
