import sys
from .mysql import mysql_get_cur
from clipboard import clipboard_write_to_clipboard, clipboard_read_from_clipboard
from pyfzf.pyfzf import FzfPrompt
from debug import DEBUG
from .converter import get_ec_field_names_for_select_in_str

def get_tables():
    cur = mysql_get_cur()
    cur.execute("SHOW TABLES")
    b = []
    for (r,) in cur:
        b.append(r)
    return b

def get_create_schema(table_name) :
    cur = mysql_get_cur()
    cur.execute("SHOW CREATE TABLE " + table_name)
    for (_, ct) in cur:
        return ct

# TODO: 複数のテーブルを作成したい。
def get_one_table():
    fzf = FzfPrompt()
    table_names = fzf.prompt(get_tables())

    assert len(table_names) > 0
    return table_names[0]

def main():
    argvlen = len(sys.argv[1:])
    cmd = "main"
    if DEBUG:
        print("argv: ", sys.argv)
    if argvlen != 0:
        cmd = sys.argv[1]
    if cmd == "main":
        table_name = get_one_table()
        if DEBUG:
            print("table name: ", table_name)

        schema = get_create_schema(table_name)
        if DEBUG:
            print("schema: ", schema)
        
        clipboard_write_to_clipboard(schema)
        if DEBUG:
            print("now clipboard: " , )
    elif cmd == "show":
        table_name = sys.argv[2]
        # table_name = get_one_table()
        if DEBUG:
            print("table name: ", table_name)

        schema = get_create_schema(table_name)
        print(schema)
    elif cmd == "select_field":
        table_name = sys.argv[2]
        suf = sys.argv[3]
        schema = get_create_schema(table_name)
        fields_string = get_ec_field_names_for_select_in_str(schema, suf)
        # print(fields)
        clipboard_write_to_clipboard(fields_string)


