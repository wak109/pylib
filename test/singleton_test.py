#!/usr/bin/env python
#

import operator
import unittest

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from singleton import *

class SingletonTest(unittest.TestCase):

    def test1(self):

        class Test(Singleton('Test', (object,), {})):

            def __init__(self, val):
                self.val = val

        inst1 = Test(1)
        inst2 = Test(2)

        self.assertEqual(inst1.val, 1)
        self.assertEqual(inst2.val, 1)
        self.assertEqual(inst1, inst2)

class SingletonDictTest(unittest.TestCase):

    def test1(self):

        class Test(SingletonDict('Test', (object,), {})):

            def __init__(self, val):
                self.val = val

        inst1 = Test(1)
        inst2 = Test(2)
        inst2a = Test(2)

        self.assertEqual(inst1.val, 1)
        self.assertEqual(inst2.val, 2)
        self.assertEqual(inst2, inst2a)

    def test2(self):

        class Test(SingletonDict('Test', (object,), {})):

            def __init__(self, a, b, c=3):
                pass

        i1 = Test(1, 2)
        i2 = Test(1, b=2, c=3)
        i3 = Test(1, 2, 3)
        i4 = Test(c=3, a=1, b=2)


        self.assertEqual(i1, i2)
        self.assertEqual(i2, i3)
        self.assertEqual(i3, i4)

        j1 = Test(1, c=2, b=3)

        self.assertNotEqual(i4, j1)

    def test3(self):

        class Test(SingletonDict('Test', (object,), {})):
            pass


        inst1 = Test()
        inst2 = Test()

        self.assertEqual(inst1, inst2)

    def test_key_args(self):

        class Test(SingletonDict('Test', (object,), {})):

            _key_args = ('a', 'b')

            def __init__(self, a, b, c):
                self.a = a
                self.b = b
                self.c = c

        i1 = Test(1, 2, 3)
        i2 = Test(1, b=2, c=4)
        i3 = Test(1, b=3, c=3)

        self.assertEqual(i2.c, 3)
        self.assertEqual(i1, i2)
        self.assertNotEqual(i1, i3)


########################################################################
# main
########################################################################

if __name__ == '__main__':
    unittest.main(verbosity=2)
