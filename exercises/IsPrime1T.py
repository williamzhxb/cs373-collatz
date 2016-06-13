#!/usr/bin/env python3

# ------------
# IsPrime1T.py
# ------------

# https://en.wikipedia.org/wiki/Primality_test

from unittest import main, TestCase

from IsPrime1 import is_prime

class MyUnitTests (TestCase) :
    def test_01 (self) :
        self.assertFalse(is_prime(1))

    def test_02 (self) :
        self.assertFalse(is_prime(2))

    def test_03 (self) :
        self.assertTrue(is_prime(3))

    def test_04 (self) :
        self.assertFalse(is_prime(4))

    def test_05 (self) :
        self.assertTrue(is_prime(5))

    def test_07 (self) :
        self.assertTrue(is_prime(7))

    def test_09 (self) :
        self.assertTrue(is_prime(9))

    def test_27 (self) :
        self.assertFalse(is_prime(27))

    def test_29 (self) :
        self.assertTrue(is_prime(29))

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage3 run --branch IsPrime1T.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
coverage3 report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
IsPrime1.py        9      0      6      0   100%
IsPrime1T.py      23      0      0      0   100%
----------------------------------------------------------
TOTAL             32      0      6      0   100%
"""
