HEADER = '\033[95m'
INFO = '\033[94m'
DEBUG = '\033[96m'
OK = '\033[92m'
WARNING = '\033[93m'
ERROR = '\033[91m'
ENDC = '\033[0m'


def info(text):
    print(INFO + "INFO: " + text + ENDC)


def debug(text):
    print(DEBUG + "DEBUG: " + text + ENDC)


def ok(text):
    print(OK + "OK: " + text + ENDC)


def warning(text):
    print(WARNING + "WARNING: " + text + ENDC)


def error(text):
    print(ERROR + "ERROR: " + text + ENDC)
