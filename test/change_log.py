import datetime
from base import ApiTest

# Endpoints data for tests
endpoints_base = "change_log"
endpoints = [
    {
        "url": "query",
        "info": "show all rows",
        "method": "get",
        "data": {}
    },
    {
        "url": "query/1",
        "info": "show the first row",
        "method": "get",
        "data": {}
    },
    {
        "url": "query/9999",
        "info": "show the 9,999 row",
        "method": "get",
        "data": {}
    },
    {
        "url": "add",
        "info": "insert new row",
        "method": "post",
        "data": {
            "gps_serial": 121212,
            "date": datetime.datetime.now(),
            "type": "sample",
            "previous_value": 0,
            "new_value": 1,
        },
    },
    {
        "url": "add",
        "info": "try to insert new row with wrong parameters",
        "method": "post",
        "data": {
            "gps": 121212,
            "d": datetime.datetime.now(),
            "t": "sample",
            "previous": 0,
            "new": 1,
        },
    },
    {
        "url": "update/1",
        "info": "update the first register",
        "method": "post",
        "data": {
            "gps_serial": 121212,
            "date": datetime.datetime.now(),
            "type": "sample",
            "previous_value": 1,
            "new_value": 2,
        },
    },
    {
        "url": "update/",
        "info": "try to update without id",
        "method": "post",
        "data": {
            "gps_serial": 121212,
            "date": datetime.datetime.now(),
            "type": "sample",
            "previous_value": 1,
            "new_value": 2,
        },
    },
    {
        "url": "update/9999",
        "info": "try to update with wrong id",
        "method": "post",
        "data": {
            "gps_serial": 121212,
            "date": datetime.datetime.now(),
            "type": "sample",
            "previous_value": 1,
            "new_value": 2,
        },
    },
    {
        "url": "update/1",
        "info": "try to update with wrong parameters",
        "method": "post",
        "data": {
            "gps": 121212,
            "d": datetime.datetime.now(),
            "t": "sample",
            "previous": 0,
            "new": 1,
        },
    },
]

if __name__ == "__main__":
    test_user = ApiTest (endpoints_base, endpoints)
    test_user.run_tests ()