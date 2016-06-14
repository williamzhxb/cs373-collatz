#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

cache = {}


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_CycleLength(n):
    # making sure n is > 0
    assert n > 0
    origin = n
    found = -1
    c = 1
    # looping checking if n is still bigger than 1
    while n > 1:
        # if n is even
        if (n % 2) == 0:
            n = (n >> 1)
            c += 1
            # after computation check again if it is in cache
            if n in cache:
                found = cache[n] + c - 1
                cache[origin] = found
                return found
        # n is odd
        else:
            n = n + (n >> 1) + 1
            c += 2
            # after computation check again if it is in cache
            if n in cache:
                found = cache[n] + c - 1
                cache[origin] = found
                return found
    # never found it in cache so add it in
    if(found == -1):
        cache[origin] = c
        return c
    # found it in cache just return
    return found


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert j > 0

    maxCycleLength = 0
    lowerBound = i

    if (j // 2) >= i:
        lowerBound = j // 2
    elif j < i:
        lowerBound = j
        j = i
    elif j == i:
        return collatz_CycleLength(i)
    # a eager cache suggested on canvas discussion by checking if max cycle
    # length number is in the range
    if lowerBound <= 837799 and j >= 837799:
        return 525
    # going through the actual range
    for n in range(lowerBound, j + 1):
        if n in cache:
            c = cache[n]
        else:
            c = collatz_CycleLength(n)
        if maxCycleLength < c:
            maxCycleLength = c
    return maxCycleLength

    return 1

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        if s == '\n':
            break
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
