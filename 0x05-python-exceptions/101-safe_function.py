#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    sum = 0
    try:
        sum = fct(args[0], args[1])
    except IndexError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except ZeroDivisionError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except TypeError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    else:
        return sum
