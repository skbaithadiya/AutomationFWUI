import pytest
import logging
import time
from selenium import webdriver
from AutomationFramework.DriverFactory.WebAgent.WebAgent import GetDriver
from AutomationFramework.Logging.Logging import LoggingUtils
from AutomationFramework.Screenshot.Screenshot import ScreenshotUtils
from TestProject import ProjectConstants


class BaseTestCase(object):

    def __init__(self):
        self.driver = GetDriver('chrome').set_driver()
        logger = LoggingUtils()
        logger.get_logger()
        

    def test_go_to_homepage(self):
        self.driver.get('https://www.gmail.com')


if __name__ == "__main__":
    driver = GetDriver('chrome').set_driver()
    url = "https://www.gmail.com"
    driver.get(url)
    logging.info('Navigating to :'+str(url))
    time.sleep(2)
    screenshot = ScreenshotUtils(driver)
    screenshot.take_screen_shot(ProjectConstants.SCREENSHOT_PATH, 'screenshot.png')
    driver.quit()
