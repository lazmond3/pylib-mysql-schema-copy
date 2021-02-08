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

# スネークケースからキャメルケースに変換する


def get_fields_in_camel_from_schema(schema_str):
    pass

# ダミーの insert を作成する。


def get_dummy_insert_from_schema(schema_str):
    pass
