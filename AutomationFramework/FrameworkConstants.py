import os

FRAMEWORK_ROOT_DIR = os.path.abspath(os.curdir)
print(FRAMEWORK_ROOT_DIR)

CHROME_WIN_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"
CHROME_OSX_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"
CHROME_LINUX_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"

FIREFOX_WIN_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"
FIREFOX_OSX_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"
FIREFOX_LINUX_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"

SAFARI_WIN_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"
SAFARI_OSX_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"
SAFARI_LINUX_PATH = FRAMEWORK_ROOT_DIR + "\AutomationFramework\Resource\drivers\windows\chromedriver.exe"

CHROME = 'chrome'
FIREFOX = 'firefox'
SAFARI = 'safari'

WINDOWS = 'windows'
LINUX = 'linux'
OSX = 'osx'

INFO = 'INFO'
DEBUG = 'debug'

LOG_FILE_NAME = 'Test.log'