#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arg_len = len(argv)
    if arg_len == 1:
        print("{} arguments.".format(arg_len-1))
    elif arg_len == 2:
        print("{} argument:".format(arg_len-1))
        print("{}: {}".format(1, argv[1]))
    elif arg_len > 2:
        print("{} arguments:".format(arg_len-1))
        for index, arg in enumerate(argv):
            print("{}: {}".format(index, arg))
