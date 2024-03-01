import json


def get_operations():
    """
    Функция для получения списка операций из файла
    :return: список операций
    """
    with open('operations.json', 'rt', encoding='utf-8') as file:
        operations_list = json.loads(file.read())
    return operations_list


def sort_operations(operations_list):
    """
    Функция для сортировки списка операций по дате
    :param operations_list: список операций
    :return: отсортированный по дате список операций
    """
    sorted_operations = sorted(operations_list, key=lambda x: x.get('date', 'Неизвестно'), reverse=True)
    return sorted_operations
