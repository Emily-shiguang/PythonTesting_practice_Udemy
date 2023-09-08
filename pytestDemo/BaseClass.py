import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # give you the name from which this method being called
        logger = logging.getLogger(loggerName)  # It will catch the test file name
        filehandler = logging.FileHandler("logfile.log")  # Where to log
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # How to log
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # filehandler object
        logger.setLevel(logging.INFO)
        return logger
