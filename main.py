from units import operations, last_5_operations, operation_info

# Получение списка операций из файла
operations_list = operations.get_operations()

# Сортировка списка по дате
operations_list = operations.sort_operations(operations_list)

# Получение 5 последних операций
operations_list = last_5_operations.get_last(operations_list)

# Вывод результатов
for i in operations_list:
    operation = operation_info.get_info(i)
    print(operation['date'], operation['description'])
    print(f"{operation['from']} -> {operation['to']}")
    print(operation['operationAmount'])
    print()
