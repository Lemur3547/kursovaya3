import json


def get():
    with open('../operations.json', 'rt', encoding='utf-8') as file:
        operations_list = json.loads(file.read())
    return operations_list


def sort(operations_list):
    sorted_operations = sorted(operations_list, key=lambda x: x.get('date', 'Неизвестно'), reverse=True)
    return sorted_operations
