from .mysql import mysql_get_cur
from clipboard import clipboard_write_to_clipboard, clipboard_read_from_clipboard
from pyfzf.pyfzf import FzfPrompt
from debug import DEBUG

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
    table_name = get_one_table()
    if DEBUG:
        print("table name: ", table_name)

    schema = get_create_schema(table_name)
    if DEBUG:
        print("schema: ", schema)
    
    clipboard_write_to_clipboard(schema)
    if DEBUG:
        print("now clipboard: " , )

