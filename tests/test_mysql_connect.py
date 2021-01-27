# -*- coding: utf-8 -*-

import unittest
from . import context
from debug import DEBUG
mysql_schema_copy = context.mysql_schema_copy



class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_connection(self):
        # Get two buffered cursors
        curA = mysql_schema_copy.mysql_get_cur()
        curB = mysql_schema_copy.mysql_get_cur()
        query = "SELECT 1+1"
        curA.execute(query)
        for (result, ) in curA:
            if DEBUG:
                print("result type: ", type(result))
            r = int(result)
            # print("result: ", result)
            assert result == 2
        query = "SHOW TABLES"
        curA.execute(query)
        for (table_name, ) in curA:
            if DEBUG:
                print("table_name: ", table_name)
                print("table_name type: ", type(table_name))
            # curB.execute("show create table %s", (table_name, ))
            curB.execute("show create table "  +table_name)
            for (tab, ct) in curB:
                if DEBUG:
                    print("ct: ", ct)
        # curB = cnx.cursor(buffered=True)



if __name__ == '__main__':
    unittest.main()
