# TODO
import re
from debug import DEBUG
# スキーマのstringから、フィールドを取得する。
from .str_util import snake_to_lower_camel, snake_to_upper_camel

def get_fields_from_schema(schema_str):
    ans = []
    for line in schema_str.split("\n"):
        line = line.strip()
        m = re.match(r" *`([a-zA-Z0-9_]+)`", line)
        if m:
            if DEBUG:
                print(m.group(1))
            ans.append(m.group(1))

    return ans

def get_ec_field_names_for_select_in_str(schema_str, suf) -> str:
    fields = get_fields_from_schema( schema_str )
    lines = []
    for f in fields:
        li = f"{suf}.{f} AS {suf}_{f}"
        lines.append(li)
    if DEBUG:
        print("lines: ", lines)
    ans_string = ",\n".join(lines)
    return ans_string

def get_fields_in_snake_comma_seperated_from_schema(schema_str):
    """フィールド名の一覧をsnake caseで取得する

    Args:
        schema_str (str): スキーマ定義
    """
    fields = get_fields_from_schema(schema_str)

    return ",\n".join(fields)

def get_table_name(schema_str):
    for line in schema_str.split("\n"):
            line = line.strip()
            m = re.match(r"CREATE TABLE `([a-zA-Z0-9_]+)`", line)
            if m:
                if DEBUG:
                    print(m.group(1))
                return m.group(1)

def get_insert_in_mybatis_simple(schema_str):
    """mybatis 単数の Insertを作成する

    Args:
        schema_str (str): CREATE SCHEMA
    """
    table_name = get_table_name(schema_str)
    snake_fields = get_fields_from_schema(schema_str)
    fields = [ "                " + l   for l in snake_fields]
    camel_fields_for_mybatis_escaped = ["                " + "#{" + snake_to_lower_camel(l) + "}" for l in snake_fields]
    script = """    @Insert(
        \"\"\"
            INSERT INTO {}
            (
{}
            )
            VALUES
            (
{}
            )
        \"\"\"
    )
    @Options(useGeneratedKeys = true, keyProperty = "{}")
    fun insert({}: {}): Int
""".format(
    table_name,
    ",\n".join(fields),
    ",\n".join(camel_fields_for_mybatis_escaped),
    snake_to_lower_camel(snake_fields[0]),
    snake_to_lower_camel(table_name),
    snake_to_upper_camel(table_name) 
)
    return script


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
