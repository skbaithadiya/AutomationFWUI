from selenium import webdriver
from AutomationFramework import FrameworkConstants
from AutomationFramework.Logging.Logging import LoggingUtils

import os, platform
import unittest
import time
import logging

class GetDriver(object):

    def __init__(self, driver_name):
        self.chrome = ChromeDriver()
        self.firefox = FirefoxDriver()
        self.safari = SafariDriver()
        self.driver_name = driver_name
        logger = LoggingUtils()
        logger.get_logger()


    def set_driver(self):
        try:
            if self.driver_name.lower() == FrameworkConstants.CHROME:
                return self.chrome.get_chrome_driver()
            elif self.driver_name.lower() == FrameworkConstants.FIREFOX:
                return self.firefox.get_firefox_driver()
            elif self.driver_name.lower() == FrameworkConstants.SAFARI:
                return self.safari.get_safari_driver()
            else:
                return "Not Supported Driver!"
        except Exception as e:
            print(e)
            return False


class ChromeDriver(object):
        
    def get_chrome_driver(self):
        try:
            print('launching chrome browser...')
            logging.info('Launching chrome browser...')
            if platform.system().lower() == FrameworkConstants.WINDOWS:
                chrome_dir = FrameworkConstants.CHROME_WIN_PATH
            elif platform.system().lower() == FrameworkConstants.LINUX:
                chrome_dir = FrameworkConstants.CHROME_LINUX_PATH
            elif platform.system().lower() == FrameworkConstants.OSX:
                chrome_dir = FrameworkConstants.CHROME_OSX_PATH
            else:
                print("Not Supported Platform!")
                return False
            # chrome browser options
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            options.add_argument("--start-maximized")
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
            self.driver = webdriver.Chrome(executable_path=chrome_dir, chrome_options=options) 
            return self.driver
        except Exception as e:
            print(e)
            return False
    
    def set_chrome_capabilities(self):
        pass

class FirefoxDriver(object):
        
    def get_firefox_driver(self):
        try:
            print('launching firefox browser...')
            logging.info('Launching firefox browser...')
            if platform.system().lower() == FrameworkConstants.WINDOWS:
                ff_dir = FrameworkConstants.FIREFOX_WIN_PATH
            elif platform.system().lower() == FrameworkConstants.LINUX:
                ff_dir = FrameworkConstants.FIREFOX_LINUX_PATH
            elif platform.system().lower() == FrameworkConstants.OSX:
                ff_dir = FrameworkConstants.FIREFOX_OSX_PATH
            else:
                print("Not Supported Platform!")
                return False
            self.driver = webdriver.Chrome(ff_dir) 
            return self.driver
        except Exception as e:
            print(e)
            return False
    def set_firefox_capabilities(self):
        pass

class SafariDriver(object):
        
    def get_safari_driver(self):
        print('launching safari browser...')
        logging.info('Launching safari browser...')
        if platform.system().lower() == FrameworkConstants.WINDOWS:
            safari_dir = FrameworkConstants.SAFARI_WIN_PATH
        elif platform.system().lower() == FrameworkConstants.LINUX:
            safari_dir = FrameworkConstants.SAFARI_LINUX_PATH
        elif platform.system().lower() == FrameworkConstants.OSX:
            safari_dir = FrameworkConstants.SAFARI_OSX_PATH
        else:
            print("Not Supported Platform!")
            return False
        self.driver = webdriver.Chrome(safari_dir) 
        return self.driver

    def set_safari_capabilities(self):
        pass


