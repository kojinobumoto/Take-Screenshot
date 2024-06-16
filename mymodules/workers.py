from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path
import time
import base64
import requests
from . import settings


settings.init()
options = Options()

options.add_argument('--headless=new')
options.page_load_strategy = 'normal'

#
# "The team owning Headleass Chrome has decided not to support extensions."...
# https://bugs.chromium.org/p/chromedriver/issues/detail?id=2342
# https://bugs.chromium.org/p/chromium/issues/detail?id=706008
#options.add_extension(mymodules.settings.auth_extension_file)
#

options.add_argument('--ignore-certificate-errors')
options.add_argument("--run-all-compositor-stages-before-draw")

driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(60)


def ts_init(str_start_datetime):
	take_screenshot.SCREENSHOT_DIR = settings.SCREENSHOT_DIR_PREFIX + '-' + str_start_datetime
	Path(take_screenshot.SCREENSHOT_DIR).mkdir(exist_ok=True, parents=True)

def quit_web_driver():
    driver.close()
    driver.quit()

def replace_chars_for_filename(text):
    for ch in ['/', '\\','`','*','{','}','>','#','!','$','\'', ';', ':']:
        if ch in text:
            text = text.replace(ch,"-")
    for ch in ['?']:
        if ch in text:
            text = text.replace(ch,"?")
    return text

def take_screenshot(index, url):

    image_filename = ""

    try:
        image_filename = str(index) + '.png'


        # cannot pass the driver object by queue since it's not picklable object.
        #driver = ts_init.q.get()

        # reset window size (especially width)
        #driver.set_window_size(1800, 10)

        # each url
        driver.get(url)
        page_width = driver.execute_script('return document.body.scrollWidth')
        page_height = driver.execute_script('return document.body.scrollHeight')
        driver.set_window_size(page_width, page_height)
        time.sleep(5)

        bool_save_result = driver.save_screenshot(take_screenshot.SCREENSHOT_DIR + '/' + image_filename)
        if bool_save_result == False:
            image_filename = f'[ERROR] Failed to save image file "{image_filename}".'
    except Exception as ex:
        image_filename = f'[ERROR] {type(ex).__name__} in {comare_image_diff.__name__} : {ex}'
     finally:
        #ts_init.q.put(driver)
        return [url, image_filename]