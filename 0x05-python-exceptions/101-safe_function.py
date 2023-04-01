#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except BaseException as er:
        res = None
        print("Exception: {}".format(er), file=sys.stderr)
    finally:
        return res
