from units import operation_info


def test_operation_info():
    assert operation_info.get_info({
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }) == {
               "date": "26.08.2019",
               "description": "Перевод организации",
               "from": "Maestro 1596 83** **** 5199",
               "to": "Счет **9589",
               "operationAmount": "31957.58 руб."
           }
    assert operation_info.get_info({
        "id": 542678139,
        "state": "EXECUTED",
        "date": "2018-10-14T22:27:25.205631",
        "operationAmount": {
            "amount": "90582.51",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 78808375133947439319",
        "to": "Visa Platinum 2256483756542539"
    }) == {
               "date": "14.10.2018",
               "description": "Перевод организации",
               "from": "Счет **9319",
               "to": "Visa Platinum 2256 48** **** 2539",
               "operationAmount": "90582.51 USD"
           }
