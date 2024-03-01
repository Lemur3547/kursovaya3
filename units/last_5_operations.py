def get_last(operations_list):
    """
    Функция для выбора 5 последних успешных операций
    :param operations_list: список операций
    :return: список из 5 последних успешных операций
    """
    last_5_operations = []
    count = 0
    while len(last_5_operations) < 5:
        if operations_list[count].get('state') == 'EXECUTED':
            last_5_operations.append(operations_list[count])
        count += 1
    return last_5_operations
