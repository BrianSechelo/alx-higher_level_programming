#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenn = len(argv) - 1
    if lenn < 1:
        print("{} arguments.".format(lenn))
    elif lenn == 1:
        print("{} argument.".format(lenn))
    else:
        print("{} arguments".format(lenn))
    for i in range(lenn):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
