
import logging
# automatically capture ur test file name test_logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)



    fileHandler=logging.FileHandler('logfile.log')
    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    #There should be connection between Fromatter and addHandler, give info about
    #formatter to fileHandler
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    # we need to set level, If I want to see only error logs

    logger.setLevel(logging.INFO)
    # in which files messages to print and in which format, send in addHandler method
    # Filehandler means file name
    logger.debug("A debug statement is executing")
    logger.info("Information Statement")
    logger.warning("Warning Statement")
    logger.error("Error Statement")
    logger.critical("Critical Statement")

