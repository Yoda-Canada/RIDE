# Automatically generated by 'package.py' script.

VERSION = 'trunk'
RELEASE = '20110901'
TIMESTAMP = '20110901-114717'

def get_version(sep=' '):
    if RELEASE == 'final':
        return VERSION
    return VERSION + sep + RELEASE
