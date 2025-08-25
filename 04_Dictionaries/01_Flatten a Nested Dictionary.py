nested_dict = {
    'user': {
        'name': 'Alice',
        'info': {
            'age': 25,
            'city': 'Delhi'
        }
    },
    'active': True
}
new = {}
for key, value in nested_dict.items():
    new[key] = nested_dict[key]

print(new)