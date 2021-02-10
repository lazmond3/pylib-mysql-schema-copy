# TODO
import re
from enum import Enum
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
        schema_str (str): CREATE SCHEMA'
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
    table_name = get_table_name(schema_str)
    arg_property_name = snake_to_lower_camel(table_name)
    snake_fields = get_fields_from_schema(schema_str)
    fields = [ "                "   +  
    l   for l in snake_fields]
    camel_fields_for_mybatis_escaped = ["                " + "#{" + 
    arg_property_name + "." + 
    snake_to_lower_camel(l) + "}" for l in snake_fields]
    script = """    @Insert(
        \"\"\"
        <script>
            INSERT INTO {}
            (
{}
            )
            VALUES
            <foreach item="{}" collection="{}" separator=",">
            (
{}
            )
            </foreach>
        </script>
        \"\"\"
    )
    @Options(useGeneratedKeys = true, keyProperty = "{}")
    fun insertAll({}: List<{}>): Int
""".format(
    table_name,
    ",\n".join(fields),
    arg_property_name, # snapshot
    snake_to_lower_camel(table_name) + "s", # snapshots
    ",\n".join(camel_fields_for_mybatis_escaped),
    snake_to_lower_camel(snake_fields[0]),
    snake_to_lower_camel(table_name),
    snake_to_upper_camel(table_name) 
)
    return script
    


def get_field_types_from_schema(schema_str):
    # primary_key = ""
    # unique key 製薬のために
    for line in schema_str.split("\n"):
        line = line.strip()
        m = re.match(r" *`PRIMARY KEY \((.*)\)`", line)
        if m:
            primary_key = m.group(1)
            continue
        m = re.match(r"UNIQUE KEY `.*` \((.*)\) ", line) 
        if m:
            in_g = m.group(1)
            if "," in in_g:


class MysqlType(Enum):
    CHAR=1
    TEXT=2
    INT=3
    DATE=4
    DATETIME=5
    FLOAT=6
    DECIMAL=7
    VARCHAR=8


class FieldType:
    """fieldargument
    """

    def __init__(self):
        self.is_unique = False
        self.is_encrypted = False
        self.is_nullable = False
        self.unique_fields = []
        self.type_length = 0 # char varchar decimal など字数制限があるもの




# src[~/github/react/create-insert]
def get_dummy_insert_sql_from_schema(schema_str):
    """dummy のsql文を作成する(最難関) 
    (すでにjsで定義しているもの)
    ref: ~/github/react/create-insert

    Args:
        schema_str (str): スキーマ定義
    """
    pass

# この関数によって 
def get_dummy_multiple_insert_sql_from_schema(schema_str, count):
    """dummy のsql文を作成する(最難関) 
    (すでにjsで定義しているもの)
    ref: ~/github/react/create-insert

        unique の処理が必要になる。
        unique の処理は、対象のフィールド名を リストで所持する。

    Args:
        schema_str (str): スキーマ定義
    """
    pass
