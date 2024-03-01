import datetime


def get_info(operation):
    operation_info = {}

    date = datetime.datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f")
    operation_info['date'] = datetime.datetime.strftime(date, "%d.%m.%Y")

    operation_info['description'] = operation.get('description', 'Неизвестная операция')

    operation_info['from'] = operation.get('from', 'Неизвестно')
    if operation_info['from'] != 'Неизвестно':
        from_str = operation_info['from'].split()
        if from_str[0] == 'Счет':
            from_str[-1] = f'**{from_str[-1][-4:]}'
        else:
            from_str[-1] = ''.join([from_str[-1][:6], '*' * (len(from_str[-1]) - 10), from_str[-1][-4:]])
            from_str[-1] = ' '.join([from_str[-1][i: i + 4] for i in range(0, len(from_str[-1]), 4)])
        operation_info['from'] = ' '.join(from_str)

    operation_info['to'] = operation['to']
    to_str = operation_info['to'].split()
    if to_str[0] == 'Счет':
        to_str[-1] = f'**{to_str[-1][-4:]}'
    else:
        to_str[-1] = ''.join([to_str[-1][:6], '*' * (len(to_str[-1]) - 10), to_str[-1][-4:]])
        to_str[-1] = ' '.join([to_str[-1][i: i + 4] for i in range(0, len(to_str[-1]), 4)])
    operation_info['to'] = ' '.join(to_str)

    operation_info['operationAmount'] = (f'{operation["operationAmount"]["amount"]} '
                                         f'{operation["operationAmount"]["currency"]["name"]}')

    return operation_info
