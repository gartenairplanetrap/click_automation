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
    print("Context: Phone")
    retry_count = 0
    while retry_count < 3:
        try:
            rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png")
            sleep(1)

            rttc.click_textdata("PHONE", button_region)

            sleep(3)

            result_phone = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Phone_Screen.png", "Phone")
            context_status["Phone"] = result_phone
            sleep(1)
            break
        except Exception as e:
            retry_count += 1
            print(f"Error {e}")

def grid():
    print("\nContext: Gridmenu")
    retry_count = 0
    while retry_count < 3:
        try:
            rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png")

            sleep(1)

            rttc.click_textdata("MENU", button_region)

            sleep(3)

            result_gridmenu = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Gridmenu_Screen.png", "Gridmenu")

            context_status["Grid"] = result_gridmenu

            sleep(1)

            break
        except Exception as e:
            retry_count += 1
            print(f"Error {e}")

def radio():
    print("\nContext: Radio")

    rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png")

    sleep(1)

    rttc.click_textdata("RADIO", button_region)

    sleep(3)

    result_radio_AM = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Radio_AM_Screen.png", "Radio_AM")
    result_radio_FM = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Radio_FM_Screen.png",  "Radio_FM")
    if result_radio_FM >= result_radio_AM:
        context_status["Radio"] = result_radio_FM
    else:
        context_status["Radio"] = result_radio_AM

    retry_count = 0
    while retry_count < 3:
        try:
            rttc.click_textbutton("Source", button_region)
            sleep(2)
            if rttc.click_textdata("FM", button_region) == 0:
                rttc.click_textdata("AM", button_region)
            pt.leftClick()
            break
        except Exception as e:
            retry_count += 1
            print(f"Error {e}")

    sleep(3)

    retry_count = 0
    while retry_count < 3:
        try:
            rtic.click_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Radio_Station_List.png")
            pt.leftClick()
            sleep(3)
            result_station_list = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Radio_Station_List.png", "Station List")
            context_status["Radio: Station List"] = result_station_list
            rtic.click_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Back.png")
            pt.leftClick()
            if not result_station_list > 70:
                retry_count += 1
            else:
                sleep(2)
                break
        except Exception as e:
            retry_count += 1
            print(f"Error {e}")
            sleep(2)

        sleep(2)

def media():
    print("\nContext: Media")
    rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png")
    sleep(1)

    rttc.click_textdata("MEDIA", button_region)

    sleep(3)

    retry_count = 0
    while retry_count < 3:
        try:
            rttc.click_textbutton("Favorites", button_region)
            pt.leftClick()
            break
        except Exception as e:
            retry_count += 1
            print(f"Error {e}")

    sleep(1)

    retry_count = 0
    while retry_count < 3:
        try:
            if rttc.click_textbutton("Details", button_region) == 0:
                rtic.click_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/Media_Details.png")
            pt.leftClick()
            break
        except Exception as e:
            retry_count += 1
            print(f"Error {e}")

    sleep(2)

    result_media = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Media_Screen.png", "Media")

    context_status["Media"] = result_media

    retry_count = 0
    while retry_count < 3:
        try:
            if rttc.click_textbutton("Settings", button_region) == 0:
                rtic.click_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/Media_Settings.png")
            pt.leftClick()
            break
        except Exception as e:
            retry_count += 1
            print(f"Error {e}")

    sleep(3)

    retry_count = 0
    while retry_count < 3:
        try:
            rttc.click_textdata("Manage", button_region)
            pt.leftClick()
            break
        except Exception as e:
            retry_count += 1
            print(f"Error {e}")

    sleep(2)

def navi():
    print("\nContext: Navi")
    rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png")
    sleep(1)

    rttc.click_textdata("NAVIGATION", button_region)

    sleep(3)

    result_navi_dest = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Navi_Dests_Screen.png", "Navi_Dest")
    result_navi_map = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Navi_Map_Screen.png", "Navi_Map")
    if result_navi_dest >= result_navi_map:
        context_status["Navi"] = result_navi_dest
    else:
        context_status["Navi"] = result_navi_map

    sleep(1)

def vehicle():
    retry_count = 0
    while retry_count < 3:
        print("\nContext: Vehicle")
        try:
            rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png")
            sleep(1)
            rttc.click_textdata("MENU", button_region)

            sleep(3)

            if rttc.click_textdata("Vehicle", button_region) == 0:
                rtic.click_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/Vehicle.png")
            pt.leftClick()

            sleep(3)

            result_Vehicle = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Vehicle_Screen.png", "Vehicle")
            context_status["Vehicle"] = result_Vehicle

            if context_status["Vehicle"] > 70:
                break

        except Exception as e:
            retry_count += 1
            print(f"Error {e}")


def settings():
    retry_count = 0
    while retry_count < 3:
        print("\nContext: Settings")
        try:
            rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png")
            sleep(1)

            rttc.click_textdata("MENU", button_region)

            sleep(3)

            if rttc.click_textdata("Settings", button_region) == 0:
                rtic.click_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/Settings.png")
            pt.leftClick()

            sleep(3)

            result_Settings = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Settings_Screen.png", "Settings")
            context_status["Settings"] = result_Settings

            if context_status["Settings"] > 70:
                break

        except Exception as e:
            retry_count += 1
            print(f"Error {e}")

def sound():
    retry_count = 0
    while retry_count < 3:
        print("\nContext: Sound")
        try:
            rtic.nav_to_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/RT_Hardkeys.png")
            sleep(1)

            rttc.click_textdata("MENU", button_region)

            sleep(3)

            if rttc.click_textdata("Sound", button_region) == 0:
                rtic.click_image("C:/Users/TimPfeiffer/Pictures/Keys_Buttons/Sound.png")
            pt.leftClick()

            sleep(2)

            rttc.click_textdata("Position", button_region)

            sleep(3)

            result_sound = comp.compare("C:/Users/TimPfeiffer/Pictures/Screens/RT_Sound_Screen.png", "Sound")
            context_status["Sound"] = result_sound

            if context_status["Sound"] > 60:
                break

        except Exception as e:
            retry_count += 1
            print(f"Error {e}")
