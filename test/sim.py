import datetime
from base import ApiTest

# Endpoints data for tests
endpoints_base = "sim"
endpoints = [
    {
        "url": "query",
        "info": "show all rows",
        "method": "get",
        "data": {}
    },
    {
        "url": "query/123456789",
        "info": "show specific row",
        "method": "get",
        "data": {}
    },
    {
        "url": "query/000000000",
        "info": "show wrong row",
        "method": "get",
        "data": {}
    },
    {
        "url": "add",
        "info": "insert new row",
        "method": "post",
        "data": {
            "telephone": "12121212",
            "account": "sample",
            "father_account": "sample father",
            "iccid": "000001",
            "package": "sample package",
            "status": "1",
            "created_by": "1"
        },
    },
    {
        "url": "add",
        "info": "try to insert new row with wrong parameters",
        "method": "post",
        "data": {
            "tel": "12121212",
            "account": "sample",
            "father": "sample father",
            "iccid": "000001",
            "pack": "sample package",
            "status": "1",
            "created": "1"
        },
    },
    {
        "url": "update/12121212",
        "info": "update the first register",
        "method": "post",
        "data": {
            "account": "updated sample",
            "father": "updated father",
            "cancellation_date": datetime.datetime.now (),
            "updated_by": "1"
        },
    },
    {
        "url": "update/",
        "info": "try to update without telephone",
        "method": "post",
        "data": {
            "account": "updated sample",
            "father": "updated father",
            "cancellation_date": datetime.datetime.now (),
            "updated_by": "1"
        },
    },
    {
        "url": "update/100000000",
        "info": "try to update with wrong telephone",
        "method": "post",
        "data": {
            "account": "updated sample",
            "father": "updated father",
            "cancellation_date": datetime.datetime.now (),
            "updated_by": "1"
        },
    },
    {
        "url": "update/12121212",
        "info": "try to update with wrong parameters",
        "method": "post",
        "data": {
            "acc": "updated sample",
            "fath": "updated father",
            "cancellation": datetime.datetime.now (),
            "updated_by": "1"
        },
    },
    {
        "url": "update/12121212",
        "info": "try to update without 'updated_by' parameter",
        "method": "post",
        "data": {
            "acc": "updated sample",
            "fath": "updated father",
            "cancellation": datetime.datetime.now (),
        },
    },
]

if __name__ == "__main__":
    test_sim = ApiTest (endpoints_base, endpoints)
    test_sim.run_tests ()