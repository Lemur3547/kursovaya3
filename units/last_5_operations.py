def get(operations_list):
    last_5_operations = []
    count = 0
    while len(last_5_operations) < 5:
        if operations_list[count].get('state') == 'EXECUTED':
            last_5_operations.append(operations_list[count])
        count += 1
    return last_5_operations
