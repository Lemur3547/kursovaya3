from units import last_5_operations


def test_last_5_operations():
    assert last_5_operations.get_last(
        [
            {"id": 41428829, "state": "EXECUTED"},
            {"id": 939719570, "state": "CANCELED"},
            {"id": 587085106, "state": "EXECUTED"},
            {"id": 142264268, "state": "CANCELED"},
            {"id": 873106923, "state": "EXECUTED"},
            {"id": 214024827, "state": "EXECUTED"},
            {"id": 522357576, "state": "EXECUTED"},
            {"id": 895315941, "state": "EXECUTED"}
        ]
    ) == [{"id": 41428829, "state": "EXECUTED"},
          {"id": 587085106, "state": "EXECUTED"},
          {"id": 873106923, "state": "EXECUTED"},
          {"id": 214024827, "state": "EXECUTED"},
          {"id": 522357576, "state": "EXECUTED"}]
