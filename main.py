from rt_image_clicker import RT_ImageClicker
from rt_text_clicker import RT_TextClicker
from comparer import Comparer
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pyautogui as pt
import context_0102
import context_0221

product_lines = {
    "target0102 LG_F307_NAR_009": {
        "images": {
            "Screens": {
                "Gridmenu": "C:/Users/TimPfeiffer/Pictures/Screens/RT_Gridmenu_Screen.png",
                "Radio_AM": "C:/Users/TimPfeiffer/Pictures/Screens/RT_Radio_AM_Screen.png",
                "Radio_FM": "C:/Users/TimPfeiffer/Pictures/Screens/RT_Radio_FM_Screen.png",
                "Media Screen": "C:/Users/TimPfeiffer/Pictures/Screens/RT_Media_Screen.png"
            },
            "Buttons": {
                "Hardkeys": "C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png",
                "Radio Station List": "C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Radio_Station_List.png",
                "Settings": "C:/Users/TimPfeiffer/Pictures/Keys_Buttons/Settings.png",
                "Details": "C:/Users/TimPfeiffer/Pictures/Keys_Buttons/Details.png"
            }
        },
    },
    "target0221 LG_F380_060": {
        "images": {
            "Screens": {
            },
            "Buttons": {
            }
        },
    }
}

if __name__ == "__main__":
    # selected_product = int(input("Please enter 1 for target0102 LG_F307_NAR_009 or 2 for target0221 LG_F380_060: "))
    # print("Change your screen to the simulator now.")

    rttc = RT_TextClicker(0.0001, 1)
    rtic = RT_ImageClicker(0.001)
    comp = Comparer()
    button_region = (0, 0, 2560, 1600)

    sleep(4)

    selected_product = 1
    if selected_product == 1:
        images = product_lines["target0102 LG_F307_NAR_009"]

        context_0102.phone()
        context_0102.grid()
        context_0102.radio()
        context_0102.media()
        context_0102.navi()
        context_0102.sound()
        context_0102.settings()
        context_0102.vehicle()

        if not context_0102.context_status.get("Radio", 0) >= 70:
            context_0102.radio()

        if not context_0102.context_status.get("Grid", 0) >= 70:
            context_0102.grid()

        print(context_0102.context_status)

    elif selected_product == 2:
        images = product_lines["target0221 LG_F380_060"]

        context_0221.phone()
        context_0221.grid()
        context_0221.radio_media()
        context_0221.navi()
        context_0221.sound()
        context_0221.settings()
        context_0221.vehicle()

    else:
        print("Product line not found.")
