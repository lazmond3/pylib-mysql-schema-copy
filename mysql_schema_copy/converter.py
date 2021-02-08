# TODO
import re

# スキーマのstringから、フィールドを取得する。


def get_fields_from_schema(schema_str):
    ans = []
    for line in schema_str.split("\n"):
        line = line.strip()
        m = re.match(r" *`([a-z0-9_]+)`", line)
        if m:
            print(m.group(1))
            ans.append(m.group(1))

    return ans


def get_fields_in_camel_from_schema(schema_str):
    """フィールド名の一覧を camel case で取得する
    (手動でmybatisしたり、SELECT文を作るため)

    Args:
        schema_str (str): スキーマ定義
    """
    pass


def get_fields_in_snake_from_schema(schema_str):
    """フィールド名の一覧をsnake caseで取得する

    Args:
        schema_str (str): スキーマ定義
    """
    pass


def get_insert_in_mybatis_simple(schema_str):
    """mybatis 単数の Insertを作成する

    Args:
        schema_str (str): CREATE SCHEM
    """
    pass


def get_insert_in_mybatis_bulk(schema_str):
    """mybatis bulk の Insertを作成する

    Args:
        schema_str (str): CREATE SCHEM
    """
    pass


# src[/Users/JP26446/github/react/create-insert]
def get_dummy_insert_sql_from_schema(schema_str):
    """dummy のsql文を作成する(最難関)
    (すでにjsで定義しているもの)
    ref: /Users/JP26446/github/react/create-insert

    Args:
        schema_str (str): スキーマ定義
    """
    pass
