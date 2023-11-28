#!/usr/bin/bash
def uppercase(str):
    for char in str:
        b = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print(b, end=" ")
    print('')
