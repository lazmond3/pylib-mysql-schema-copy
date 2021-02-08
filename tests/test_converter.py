# -*- coding: utf-8 -*-

import unittest
from . import context
from debug import DEBUG
mysql_schema_copy = context.mysql_schema_copy
converter = mysql_schema_copy.converter


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_fields(self):
        lst = converter.get_fields_from_schema("""CREATE TABLE `Post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `published` tinyint(1) NOT NULL DEFAULT '0',
  `authorId` int DEFAULT NULL,
  `categoryId` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `authorId` (`authorId`),
  KEY `categoryId` (`categoryId`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`authorId`) REFERENCES `User` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
""")
        ans = ["id", "title", "content", "published", "authorId", "categoryId"]
        for l, r in zip(lst, ans):
            assert l == r


if __name__ == '__main__':
    unittest.main()
