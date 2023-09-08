import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)  # It will catch the test file name

    filehandler = logging.FileHandler("logfile.log")  # Where to log
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # How to log
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)  # filehandler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Somthing is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")