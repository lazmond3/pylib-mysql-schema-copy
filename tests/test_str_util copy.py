# -*- coding: utf-8 -*-

import unittest
from . import context
from debug import DEBUG
mysql_schema_copy = context.mysql_schema_copy
str_util = mysql_schema_copy.str_util


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_camel_to_snake_1(self):
        assert str_util.camel_to_snake("CamelCaseName") == "camel_case_name"

    def test_snake_to_camel(self):
        assert str_util.snake_to_camel("camel_case_name") == "camelCaseName"
        assert str_util.snake_to_upper_camel(
            "camel_case_name") == "CamelCaseName"


if __name__ == '__main__':
    unittest.main()
