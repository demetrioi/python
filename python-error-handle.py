# The complete script/file
import logging
import logging.handlers as r
from datetime import datetime
import pyodbc
import sys

# Function that parse/save log error to 50MB files
# This function keeps 20 files of 50 each. Recycling when necessary
# Log Name Pattern:
# YOUR_MODULE_NAME-2020-11-15.log - Actual
# YOUR_MODULE_NAME-2020-11-15.log.1 - old
# YOUR_MODULE_NAME-2020-11-15.log.2 - old
# ...
# YOUR_MODULE_NAME-2020-11-15.log.50 - old


def log_tofile(ex, path):

    logging.basicConfig(
        handlers=[r.RotatingFileHandler(
            path, maxBytes=500000, backupCount=20)],
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')

    logging.debug(ex)


conn_str = 'CONN_STR'
path = "/Volumes/GoogleDrive/My Drive/gitmac/demetrio/python/YOUR_MODULE_NAME-{:%Y-%m-%d}.log".format(
    datetime.now())

try:
    conn = pyodbc.connect(conn_str)
except:
    #  sys.exit('ERROR: Could not connect to the database')  Pls don't do this. This exception doesn't generate usefull log information
    log_tofile(sys.exc_info(), path)

# Error output sample

'''
[2020-11-15T20:32:38] DEBUG [root.log_tofile:27] (<class 'pyodbc.InterfaceError'>, InterfaceError('IM002', '[IM002] [unixODBC][Driver Manager]Data source name not found and no 
default driver specified (0) (SQLDriverConnect)'), <traceback object at 0x1017ded80>)
'''
