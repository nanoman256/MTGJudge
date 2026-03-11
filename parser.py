import re

def parse_rules(file_path, pattern):
    with open(file_path, encoding="utf-8", errors="ignore") as f:
        rules = f.read()
    return re.findall(pattern, rules, flags=re.MULTILINE)