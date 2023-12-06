#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "h", "m", "o", "r"}
    b = {"j", "k", "o", "u", "y"}
    c = {"g", "h", "j"}
    d = {"g", "j", "q"}

    bn = u.difference(b)

    x = (a.difference(c)).intersection(bn)
    print(f"x = {x}")

    y = (a.intersection(bn)).union((c.difference(d)))
    print(f"y = {y}")
