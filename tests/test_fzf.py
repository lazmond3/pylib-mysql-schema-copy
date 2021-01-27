# -*- coding: utf-8 -*-

import unittest
from . import context
from debug import DEBUG
mysql_schema_copy = context.mysql_schema_copy

import mysql.connector
from pyfzf.pyfzf import FzfPrompt


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_fzf(self):
        ls = [1,2,3,4,5,6]
        fzf = FzfPrompt()
        # print("result: ", fzf.prompt(ls))


if __name__ == '__main__':
    unittest.main()
