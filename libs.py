DATA1 = [
    ('case1:test1', {
        "output": {},
        "input": [],
    },
     "",
     False
     ),
    ('case2:test2', {
        "output": {"key": "value"},
        "input": [
            {"number": 1},
            {"number": 2},
            {"number": 3},
            {"number": 4},
        ],
    },
     """1
Found
4
9
16
""", True
     ),
    ('case3:test3', {
        "output": {"key": "value"},
        "input": [
            {"number": 4},
            {"number": 5},
            {"number": 6},
            {"number": 7},
        ],
    },
     """16
25
36
49
""", True
     ),
]


def get_data():
    return {"key": "value"}


def get_data_list():
    return [
        {"number": 1},
        {"number": 2},
        {"number": 3},
        {"number": 4},
    ]
