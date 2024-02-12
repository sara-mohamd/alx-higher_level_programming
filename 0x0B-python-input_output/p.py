#!/usr/bin/python3
import json

json_dict = """{
    "id": 12,
    "name": "John",
    "places": ["San Francisco", "Tokyo"],
    "is_active": true,
    "info": {
        "age": 36,
        "average": 3.14
    }
}"""

print(type(json_dict))


data = json.loads(json_dict)
print(data)