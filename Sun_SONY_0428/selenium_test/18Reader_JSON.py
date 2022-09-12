import json
with open('d:/Sun/python3_test/material/json.json', 'r') as f:
    data = f.read()
user_list = json.loads(data)
print(user_list)