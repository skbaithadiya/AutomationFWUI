import logging
from AutomationFramework import FrameworkConstants

class LoggingUtils(object):

    def get_logger(self):
        logging.basicConfig(
            filename=FrameworkConstants.LOG_FILE_NAME,
            format='%(asctime)s %(message)s',
            filemode='w'
        )
        self.logger = logging.getLogger()
        self.logger.setLevel(FrameworkConstants.INFO)
        return self.logger
