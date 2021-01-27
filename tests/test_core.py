# -*- coding: utf-8 -*-

import unittest
from . import context
mysql_schema_copy = context.mysql_schema_copy

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_hello(self):
        mysql_schema_copy.hello()
        assert True

if __name__ == '__main__':
    unittest.main()
