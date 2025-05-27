#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of, or if obj is an instance of a class
    that inherited from, the specified class a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class or a subclass; False otherwise.
    """
    return isinstance(obj, a_class)
