#!/usr/bin/python3
def remove_chr_at(str, n):
    recent = ''
    j = 0
    for c in str:
        if j != n:
            recent += str[j]
        j += 1
    return recent
