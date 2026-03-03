#!/usr/bin/python3
import sys
import os
import re
import json
import requests
from datetime import datetime
from html import unescape

# ----------------------------------------
# 1️⃣ Get argument date or get today date
# ----------------------------------------
if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    arg = datetime.today().strftime("%Y-%m-%d")

# -----------------------------------------
# 2️⃣ Get JSON from FreeCodeCamp Challenge
# -----------------------------------------
url = f"https://api.freecodecamp.org/daily-coding-challenge/date/{arg}"

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    json_data = response.json()
except Exception as e:
    sys.exit(f"Error to obtain JSON data: {e}")

# ------------------------------
# 3️⃣ Set Challenge description
# ------------------------------
description = re.sub(r'<[^>]+>', '', json_data.get('description', ''))
description = "# " + description.replace("\n", "\n# ")

# -------------------------------
# 4️⃣ Set function and variables
# -------------------------------
function_content = json_data['python']['challengeFiles'][0]['contents']
test_function = ""

match_name = re.search(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', function_content)
function_name = match_name.group(1) if match_name else None

match_vars = re.search(r'def\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\((.*?)\)', function_content)
function_vars = [v.strip() for v in match_vars.group(1).split(',')] if match_vars else []

if function_name and function_vars:
    test_function = f"{function_name}("
    test_function += ", ".join(f"test['parameters'][{i}]" for i in range(len(function_vars)))
    test_function += ")"

# ------------------------------
# 5️⃣ Get Challenge result type
# ------------------------------
test_code = json_data['python']['tests'][0]['text']
result_format = "unknown"

match_result = re.search(r'should return <code>(.*?)</code>', test_code)
if match_result:
    return_value = match_result.group(1).strip()
    if return_value in ['True', 'False']:
        result_format = 'bool'
    elif return_value == 'None':
        result_format = 'NoneType'
    elif re.match(r'^\[.*\]$', return_value, re.S):
        result_format = 'list'
    elif re.match(r'^\{.*\}$', return_value, re.S):
        result_format = 'dict'
    elif re.match(r'^\(.*\)$', return_value, re.S):
        result_format = 'tuple'
    elif re.match(r'^[0-9]+$', return_value):
        result_format = 'int'
    elif re.match(r'^[0-9]*\.[0-9]+$', return_value):
        result_format = 'float'
    elif re.match(r'^["\'].*["\']$', return_value):
        result_format = 'str'

# ------------------------
# 6️⃣ Get Challenge tests
# ------------------------
unit_test_lines = []
for test in json_data['python']['tests']:
    test_string = test['testString']
    m = re.search(r'(\w+)\((.+)\),\s*(.+)\)', test_string)
    if m:
        function_args = m.group(2)
        expected = m.group(3)
        params = function_args.strip()
        pos = params.rfind("(")
        if pos != -1: params = params[pos + 1:]
        result_value = expected.strip()
        result_value = result_value.replace(')`', '')
        line = f'{{"parameters": [{params}], "result": {result_value}}},'
        unit_test_lines.append("        " + line)

unit_test = "\n".join(unit_test_lines)

# -------------------
# 7️⃣ Set TPL values
# -------------------
tpl_values = {
    '{{ date }}': arg,
    '{{ title }}': json_data.get('title', ''),
    '{{ challenge_url }}': f'https://www.freecodecamp.org/learn/daily-coding-challenge/{arg}',
    '{{ description }}': description,
    '{{ function }}': function_content,
    '{{ parameters_format }}': 'list',
    '{{ result_format }}': result_format,
    '{{ unittest }}': unit_test,
    '{{ test_function  }}': test_function
}

# Read TPL
tpl_path = os.path.join(os.path.dirname(__file__), 'daily.tpl')
with open(tpl_path, 'r', encoding='utf-8') as f:
    tpl = f.read()

# Replace TPL variables
for key, value in tpl_values.items():
    tpl = tpl.replace(key, value)

# ----------------
# 8️⃣ Save result
# ----------------
date_obj = datetime.strptime(arg, "%Y-%m-%d")
path = os.path.join(os.path.dirname(__file__), 'challenges', date_obj.strftime("%Y-%m"))
os.makedirs(path, exist_ok=True)

file_name = f"{date_obj.strftime('%d')}_{json_data['title'].lower().replace(' ', '-')}.py"
file_path = os.path.join(path, file_name)

# Check, if target file exist, the action
if os.path.exists(file_path):
    print("Do you want to overwrite the file or execute it?")
    print("  [o] Overwrite")
    print("  [e] Execute")

    choice = input("Choose an option [o/e]: ").strip().lower()

    match choice:
        case "o":
            pass  # Do nothing
        case "e":
            print(f"Executing {file_path}...\r\r")
            os.system(f"{sys.executable} " + file_path)
            sys.exit()
        case _:
            print("Invalid option. Exiting.")
            sys.exit()

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(tpl)

print(f"> File saved in {file_path}")
