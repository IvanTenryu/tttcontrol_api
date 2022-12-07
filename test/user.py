from base import ApiTest

# Endpoints data for tests
endpoints_base = "user"
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
            "name": "sample name",
            "login": "sample login",
            "password": "samplepass123**",
            "user_type": 1,
            "status": 1,
            "created_by": 1,
        },
    },
    {
        "url": "add",
        "info": "try to insert new row with wrong parameters",
        "method": "post",
        "data": {
            "n": "sample name",
            "log": "sample login",
            "pass": "samplepass123**",
            "user": 1,
            "stat": 1,
            "created": 1,
        },
    },
    {
        "url": "update/1",
        "info": "update the first register",
        "method": "post",
        "data": {
            "name": "name updated",
            "login": "login updated",
            "password": "updatedpass123**",
            "updated_by": 1,
        },
    },
    {
        "url": "update/",
        "info": "try to update without id",
        "method": "post",
        "data": {
            "name": "name updated",
            "login": "login updated",
            "password": "updatedpass123**",
            "updated_by": 1,
        },
    },
    {
        "url": "update/9999",
        "info": "try to update with wrong id",
        "method": "post",
        "data": {
            "name": "name updated",
            "login": "login updated",
            "password": "updatedpass123**",
            "updated_by": 1,
        },
    },
    {
        "url": "update/1",
        "info": "try to update with wrong parameters",
        "method": "post",
        "data": {
            "n": "name updated",
            "log": "login updated",
            "pass": "updatedpass123**",
            "updated_by": 1,
        },
    },
    {
        "url": "update/1",
        "info": "try to update without 'updated_by' parameter",
        "method": "post",
        "data": {
            "n": "name updated",
            "log": "login updated",
            "pass": "updatedpass123**",
        },
    },
]

if __name__ == "__main__":
    test_user = ApiTest (endpoints_base, endpoints)
    test_user.run_tests ()