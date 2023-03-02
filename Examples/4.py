#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # open the file2.txt in read mode. causes error if no such file exists.
    with open("../txt/file2.txt", "r") as fileptr:
        # running a for loop
        for i in fileptr:
            print(i)  # i cЫontains each line of the file