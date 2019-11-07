from functools import partialmethod
from AutomationFramework import FrameworkConstants
from AutomationFramework.Logging.Logging import LoggingUtils

import logging


class ScreenshotUtils(object):

    def __init__(self, driver):
        self.driver = driver
        logger = LoggingUtils()
        logger.get_logger()

    def take_screen_shot(self, path, filename):
        self.driver.get_screenshot_as_file(path + str("\\") + filename)
        logging.info("Screenshot: '" + str(filename) + "' saved at: " + str(path))