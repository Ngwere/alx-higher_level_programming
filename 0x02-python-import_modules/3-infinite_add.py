#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    index = 1
    sum = 0
    if argv_count == 1:
        sum = argv_count
    else:
        while index  <= argv_count:
            sum += int(sys.argv[index])
            index += 1
    print("{:d}".format(sum))
