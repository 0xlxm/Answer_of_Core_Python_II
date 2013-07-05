#! /usr/bin/env python

# Version 1
def safe_floatV1(obj):
    try:
        return float(obj)
    except ValueError:
        pass

# Version 2
def safe_floatV1(obj):
    try:
        return float(obj)
    except ValueError:
        retval = None
    return retval

# Version 3
def safe_floatV1(obj):
    try:
        return float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    return retval

# Version 4
def safe_floatV1(obj):
    try:
        return float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval = 'obj Type canot be converted to float'
    return retval

# Version 5
def safe_floatV1(obj):
    try:
        return float(obj)
    except (ValueError, TypeError):
        retval = 'Argument must be a number or numeric string'
    return retval


