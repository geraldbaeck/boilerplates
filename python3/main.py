#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT_NAME
DESCRIPTION

Usage: SCRIPT_NAME.py [-hv]
       SCRIPT_NAME.py [--logLevel=<LOGLEVEL>][--environment=<ENV>]

Options:
  -h --help             Show this screen.
  -v --version          Show version.
  --logLevel=LOGLEVEL   The level of the logging output  [default: INFO]
  --environment=ENV     The execution environment
                        (development, staging or production)  [default: development]
"""

__appname__ = "APPLICATION_NAME"
__author__  = "Gerald Bäck (https://github.com/geraldbaeck/)"
__version__ = "0.0.1"
__license__ = "UNLICENSE"

DEFAULT_LOGLEVEL    = "INFO"
DEFAULT_ENVIRONMENT = "development"

# System libraries
import logging

# 3rd party libraries
from docopt import docopt
import logzero
from logzero import logger

# Own libraries

def set_up_logging(loglevel=DEFAULT_LOGLEVEL, logtofile=True):
    try:
        # setup `logzero` module
        logzero.loglevel(getattr(logging, loglevel))

        # Rotating logfile with 3 rotations, each with 1MB max size
        if logtofile:
            logzero.logfile(
                "log/{!s}.log".format(__file__.replace(".py", "")),
                maxBytes=1e6,
                backupCount=3)

    except AttributeError:
        raise Exception(
            "Unsupported logLevel. Use [DEBUG, INFO, WARNING, ERROR, CRITICAL]")


def main():
    """ Main entry point of the app """
    logger.info("hello world")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    arguments = docopt(__doc__, version=__version__)
    ENVIRONMENT = arguments['--environment']
    set_up_logging(arguments['--logLevel'])
    logger.debug("{!s} started".format(__appname__))
    main()
