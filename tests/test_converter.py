# -*- coding: utf-8 -*-

import unittest
from . import context
from debug import DEBUG
mysql_schema_copy = context.mysql_schema_copy
converter = mysql_schema_copy.converter

SCHEMA = """CREATE TABLE `post` (
  `post_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `published` tinyint(1) NOT NULL DEFAULT '0',
  `author_id` int DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`post_id`),
  KEY `author_id` (`author_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `User` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
"""


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_fields(self):
        lst = converter.get_fields_from_schema(SCHEMA)
        ans = ["post_id", "title", "content", "published", "author_id", "category_id"]
        for l, r in zip(lst, ans):
            assert l == r

    def test_get_ec_field_names_for_select_in_str(self):
        ans_lines = [
            "pos.post_id AS pos_post_id",
            "pos.title AS pos_title",
            "pos.content AS pos_content",
            "pos.published AS pos_published",
            "pos.author_id AS pos_author_id",
            "pos.category_id AS pos_category_id"
        ]
        ans_string = ",\n".join(ans_lines)
        assert ans_string == converter.get_ec_field_names_for_select_in_str(SCHEMA, "pos")

    def test_get_fields_in_snake_comma_seperated_from_schema(self):
        ans_lines = [
            "post_id",
            "title",
            "content",
            "published",
            "author_id",
            "category_id"
        ]
        assert ",\n".join(ans_lines) == converter.get_fields_in_snake_comma_seperated_from_schema(SCHEMA)

    def test_get_table_name(self):
        assert "post" == converter.get_table_name(SCHEMA)
    def test_get_insert_in_mybatis_simple(self):
        ans = """    @Insert(
        \"\"\"
            INSERT INTO post
            (
                post_id,
                title,
                content,
                published,
                author_id,
                category_id
            )
            VALUES
            (
                #{postId},
                #{title},
                #{content},
                #{published},
                #{authorId},
                #{categoryId}
            )
        \"\"\"
    )
    @Options(useGeneratedKeys = true, keyProperty = "postId")
    fun insert(post: Post): Int
"""
        result = converter.get_insert_in_mybatis_simple(SCHEMA)
        assert result == ans
    def test_get_insert_in_mybatis_bulk(self):
        ans = """    @Insert(
        \"\"\"
        <script>
            INSERT INTO post
            (
                post_id,
                title,
                content,
                published,
                author_id,
                category_id
            )
            VALUES
            <foreach item="post" collection="posts" separator=",">
            (
                #{post.postId},
                #{post.title},
                #{post.content},
                #{post.published},
                #{post.authorId},
                #{post.categoryId}
            )
            </foreach>
        </script>
        \"\"\"
    )
    @Options(useGeneratedKeys = true, keyProperty = "postId")
    fun insertAll(post: List<Post>): Int
"""
        result = converter.get_insert_in_mybatis_bulk(SCHEMA)
        assert ans == result

    def test_get_repeatedly_columns(self):
        ans = [
            "find_id",
            "result_id",
            "test_id"
        ]
        assert ans == converter.get_repeatedly_columns("(`find_id`, `result_id`, `test_id`)")

    def test_get_repeatedly_columns_single(self):
        ans = [
            "find_id"
        ]
        assert ans == converter.get_repeatedly_columns("(`find_id`)")

if __name__ == '__main__':
    unittest.main()
