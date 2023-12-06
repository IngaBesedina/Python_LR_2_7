#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = set(input("Первая строка: "))
    b = set(input("Вторая строка: "))

    c = a.intersection(b)
    print("Общие символы:", c)


