# -*- coding: utf-8 -*-

import unittest
from . import context
from debug import DEBUG
mysql_schema_copy = context.mysql_schema_copy
converter = mysql_schema_copy.converter

SCHEMA = """CREATE TABLE `Post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `published` tinyint(1) NOT NULL DEFAULT '0',
  `author_id` int DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `User` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
"""


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_fields(self):
        lst = converter.get_fields_from_schema(SCHEMA)
        ans = ["id", "title", "content", "published", "author_id", "category_id"]
        for l, r in zip(lst, ans):
            assert l == r

    def test_get_ec_field_names_for_select_in_str(self):
        ans_lines = [
            "pos.id AS pos_id",
            "pos.title AS pos_title",
            "pos.content AS pos_content",
            "pos.published AS pos_published",
            "pos.author_id AS pos_author_id",
            "pos.category_id AS pos_category_id"
        ]
        ans_string = ",\n".join(ans_lines)
        if DEBUG:
            print("anstarget: ", ans_lines)
            print(ans_string)
            print("get: ")
            print(converter.get_ec_field_names_for_select_in_str(SCHEMA, "pos"))
        assert ans_string == converter.get_ec_field_names_for_select_in_str(SCHEMA, "pos")

    def test_get_fields_in_snake_comma_seperated_from_schema(self):
        ans_lines = [
            "id",
            "title",
            "content",
            "published",
            "author_id",
            "category_id"
        ]
        assert ",\n".join(ans_lines) == converter.get_fields_in_snake_comma_seperated_from_schema(SCHEMA)

    def test_get_table_name(self):
        assert "Post" == converter.get_table_name(SCHEMA)
    def test_get_insert_in_mybatis_simple(self):
        ans = """    @Insert(
        \"\"\"
            INSERT INTO Post
            (
                id,
                title,
                content,
                published,
                author_id,
                category_id
            )
            VALUES
            (
                #{id},
                #{title},
                #{content},
                #{published},
                #{authorId},
                #{categoryId}
            )
        \"\"\"
"""

        assert converter.get_insert_in_mybatis_simple(SCHEMA) == ans

if __name__ == '__main__':
    unittest.main()
