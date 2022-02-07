#!/usr/bin/python3
"""inherits_from
"""

def inherits_from(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class
    Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
     if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
