#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arg_len = len(argv)
    summ = 0
    for index in range(1, arg_len):
        summ += int(argv[index])
    print("{}".format(summ))
