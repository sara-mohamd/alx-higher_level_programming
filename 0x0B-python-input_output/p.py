
import json

my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
# Encoding => serialize from pyhon object to json formatt dumps(), dump(, )
# Decoding => deserialize object from json formatt to python object loads()
with open('learn.json', 'r') as file:

    # file.write(json.dumps(my_dict))
    x = json.load(file)

print(x)


# with open('learn.json', 'r') as file:
#     my_dict = json.load(file)

# print(my_dict)
