#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":
    code = [] # Переменная для кода без комментариев
    py_file = input("Enter the pythone file name: ")
    txt_file = input("Enter the txt file name: ")

    with open(py_file, "r") as fileptr:
        for i in fileptr:
            if i.find('#') != -1: # Поиск начала комментария
                code.append(i[:i.find('#')]+'\n')
                continue
            code.append(i)

    with open(txt_file, "w") as fileptr:
        for item in code:
            fileptr.write(item)
