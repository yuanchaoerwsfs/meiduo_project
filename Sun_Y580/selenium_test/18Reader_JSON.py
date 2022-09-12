import json
with open('d:/python3-test/material/json.json', 'r') as f:
    data = f.read()
user_list = json.loads(data)
print(user_list)