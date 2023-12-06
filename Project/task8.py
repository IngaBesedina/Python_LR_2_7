#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("aeiouy")

    line = input("Строка: ")

    cnt = len([s for s in line if s in u])
    print("Гласных букв в строке:", cnt)
