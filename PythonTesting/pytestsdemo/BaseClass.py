import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        # There should be connection between Fromatter and addHandler, give info about
        # formatter to fileHandler
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        # we need to set level, If I want to see only error logs

        logger.setLevel(logging.DEBUG)
        return logger