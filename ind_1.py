#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    quotes = []  # Пустой список цитат

    # open the file file2.txt in read mode
    with open("txt/ind_1.txt", "r", encoding="utf8") as fileptr:
        # Построчно читаем файл
        for i in fileptr:
            start_Index = i.find('"')  # Поиск первой кавычки
            while start_Index != -1:
                end_Index = i.find('"', start_Index + 1)
                if start_Index != -1 and end_Index != -1:  # Если обе найдены
                    quotes.append(i[start_Index : end_Index + 1])
                    start_Index = i.find('"', end_Index + 1)
    # При вызове функции можно использовать оператор * для
    # распаковки итерируемого объекта в аргументы вызова:
    print(*quotes, sep="\n")
