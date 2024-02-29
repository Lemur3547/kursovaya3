import json


def get():
    with open('../operations.json', 'rt', encoding='utf-8') as file:
        operations_list = json.loads(file.read())
    return operations_list



