#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    quotes = []  # Пустой список цитат

    # open the file file2.txt in read mode
    with open("txt/ind_1.txt", "r", encoding="utf8") as fileptr:
        # Построчно читаем файл
        for i in fileptr:
            startIndex = i.find('"')  # Поиск первой кавычки
            while startIndex != -1:
                endIndex = i.find('"', startIndex + 1)
                if startIndex != -1 and endIndex != -1:  # Если обе найдены
                    quotes.append(i[startIndex : endIndex + 1])
                    startIndex = i.find('"', endIndex + 1)
    # При вызове функции можно использовать оператор * для
    # распаковки итерируемого объекта в аргументы вызова:
    print(*quotes, sep="\n")
