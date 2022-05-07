#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_empty(self):
        testcase= ""
        expected= ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

#Best of Unit Testing Standard Library Module
#Understand a Basic Example:
#
#https://docs.python.org/3/library/unittest.html#basic-example
#
#Understand how to run the tests using the Command Line:
#
#https://docs.python.org/3/library/unittest.html#command-line-interface
#
#Understand various Unit Test Design Patterns:
#
#https://docs.python.org/3/library/unittest.html#organizing-test-code
#
#Understand the uses of setUp, tearDown; setUpModule and tearDownModule
#
#Understand more specific assertions such as assertRaises
#
#https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises

#Check out the following links for more information:
#
#https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/
#
#https://landing.google.com/sre/sre-book/chapters/testing-reliability/
#
#https://testing.googleblog.com/2007/10/performance-testing.html
#
#https://www.guru99.com/smoke-testing.html
#
#https://www.guru99.com/exploratory-testing.html
#
#https://testing.googleblog.com/2008/09/test-first-is-fun_08.html

#Handling Errors Cheat-Sheet
#Raise allows you to throw an exception at any time.
#
#https://docs.python.org/3/tutorial/errors.html#raising-exceptions
#
#Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
#
#https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
#
#https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python
#
#The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.
#
#In the try clause, all statements are executed until an exception is encountered.
#
#https://docs.python.org/3/tutorial/errors.html#handling-exceptions
#
#Except is used to catch and handle the exception(s) that are encountered in the try clause.
#
#https://docs.python.org/3/library/exceptions.html#bltin-exceptions
#
#Other interesting Exception handling readings:
#
#https://doughellmann.com/posts/python-exception-handling-techniques/
