import json

data = {"name": "Avinash", "role": "Developer"}

# Encode
json_data = json.dumps(data)

# Decode
decoded_data = json.loads(json_data)

print(json_data)       # {"name": "Avinash", "role": "Developer"}
print(decoded_data)    # {'name': 'Avinash', 'role': 'Developer'}
