#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SCRIPT_NAME_HERE
DESCRIPTION_HERE

Usage: SCRIPT_NAME_HERE.py [-hv]
       SCRIPT_NAME_HERE.py [--logLevel=<LOGLEVEL>][--environment=<ENV>]

Options:
  -h --help             Show this screen.
  -v --version          Show version.
  --logLevel=LOGLEVEL   The level of the logging output  [default: INFO]
  --environment=ENV     The execution environment
                        (development, staging or production)  [default: development]
"""

__appname__ = "APPLICATION_NAME_HERE"
__author__  = "Gerald Bäck (https://github.com/geraldbaeck/)"
__version__ = "0.0pre0"
__license__ = "UNLICENSE"

DEFAULT_LOGLEVEL    = "INFO"
DEFAULT_ENVIRONMENT = "development"

import logging
from sys import exit, stderr

# 3rd party libraries
from docopt import docopt
from rainbow_logging_handler import RainbowLoggingHandler


def set_up_logging(loglevel=DEFAULT_LOGLEVEL):
    try:
        if loglevel is None:
            loglevel=DEFAULT_LOGLEVEL
        # setup `logging` module
        logger = logging.getLogger(__appname__)
        logger.setLevel(getattr(logging, loglevel))
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s]: %(message)s")  # same as default

        # setup `RainbowLoggingHandler`
        handler = RainbowLoggingHandler(
            stderr, color_funcName=('black', 'yellow', True))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

    except AttributeError:
        raise Exception(
            "Unsupported logLevel. Use [DEBUG, INFO, WARNING, ERROR, CRITICAL]")


def main():
    pass

if __name__ == "__main__":
    arguments = docopt(__doc__, version=__version__)
    ENVIRONMENT = arguments['--environment']
    logger = set_up_logging(arguments['--logLevel'])
    logger.debug("%s started".format(__appname__))
    main()
