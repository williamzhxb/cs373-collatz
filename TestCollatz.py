#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_CycleLength

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    #adding more tests
    def test_read(self):
        s = "22 220\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 22)
        self.assertEqual(j, 220)

    def test_read(self):
        s = "55 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 55)
        self.assertEqual(j, 10)

    def test_read(self):
        s = "5 110\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  5)
        self.assertEqual(j, 110)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    #adding more tests

    def test_eval_5(self):
        v = collatz_eval(50, 50)
        self.assertEqual(v, 25)

    def test_eval_6(self):
        v = collatz_eval(500, 500)
        self.assertEqual(v, 111)

    def test_eval_7(self):
        v = collatz_eval(424, 424)
        self.assertEqual(v, 15)

    def test_eval_8(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    #adding more tests
    def test_print1(self):
        w = StringIO()
        collatz_print(w, 5, 15, 25)
        self.assertEqual(w.getvalue(), "5 15 25\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 99, 110, 120)

        self.assertEqual(w.getvalue(), "99 110 120\n")
    def test_print3(self):
        w = StringIO()
        collatz_print(w, 46, 140, 220)
        self.assertEqual(w.getvalue(), "46 140 220\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    #adding more tests

    def test_solve1(self):
        r = StringIO("765 821\n43 100\n12 45\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "765 821 153\n43 100 119\n12 45 112\n")

    def test_solve2(self):
        r = StringIO("31 14\n68 31\n68 54\n88 86\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "31 14 112\n68 31 113\n68 54 113\n88 86 31\n")

    def test_solve3(self):
        r = StringIO("7 7\n15 15\n17 17\n3 3\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "7 7 17\n15 15 18\n17 17 13\n3 3 8\n")

    def test_solve4(self):
        r = StringIO("3 5\n57 154\n9 87\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "3 5 8\n57 154 122\n9 87 116\n")

    #adding tests for my own functions
    def test_cycleLength1(self):
        s = 5
        i = collatz_CycleLength(s)
        self.assertEqual(i,  6)

    def test_cycleLength2(self):
        s = 22
        i = collatz_CycleLength(s)
        self.assertEqual(i,  16)

    def test_cycleLength3(self):
        s = 55
        i = collatz_CycleLength(s)
        self.assertEqual(i,  113)

    def test_cycleLength4(self):
        s = 222
        i = collatz_CycleLength(s)
        self.assertEqual(i,  71)




# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
