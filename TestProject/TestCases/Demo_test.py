import pytest
from selenium import webdriver
from AutomationFramework.DriverFactory.WebAgent.WebAgent import GetDriver


class TestCase1(object):

    def __init__(self):
        self.driver = GetDriver('chrome').set_driver()


    def test_testcase1_test(self):
        self.driver.get('https://www.gmail.com')

if __name__ == "__main__":
    driver = GetDriver('chrome').set_driver()
    driver.get('https://www.gmail.com')





    



