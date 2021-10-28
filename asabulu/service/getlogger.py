
import logging
import logging.handlers as handlers
import os
import time

# https://www.itread01.com/content/1563349863.html

def getlogger(name: str):

    level = logging.DEBUG
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(name)
    logger.setLevel(level)

    os.makedirs(f"log/{name}", exist_ok=True)

    fileHandler = handlers.TimedRotatingFileHandler(f'log/{name}/{name}.log', when='midnight', interval=1, backupCount=30)
    fileHandler.suffix = "%Y_%m%d.log"
    fileHandler.setLevel(level)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    cmdHandler = logging.StreamHandler()
    cmdHandler.setFormatter(formatter)
    cmdHandler.setLevel(level)
    logger.addHandler(cmdHandler)

    return logger
