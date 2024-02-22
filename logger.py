#https://github.com/Delgan/loguru

import sys
from loguru import logger

logger.debug("That's it, beautiful and simple logging!")
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

# Caution, "diagnose=True" is the default and may leak sensitive data in prod
logger.add("out.log", backtrace=True, diagnose=True)

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, 1)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)