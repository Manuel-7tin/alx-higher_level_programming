#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print("Exception:", err, file=sys.stderr)
        return False
    except TypeError as err:
        print("Exception:", err, file=sys.stderr)
        return False
    else:
        return True
