import datetime
from base import ApiTest

# Endpoints data for tests
endpoints_base = "gps"
endpoints = [
    {
        "url": "query",
        "info": "show all rows",
        "method": "get",
        "data": {}
    },
    {
        "url": "query/121212",
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
            "serial": "121212",
            "imei":"1",
            "description":"sample description",
            "software_version":"sample",
            "firmware_version":"sample",
            "status":"1",
            "comments":"sample comment",
            "sim_telephone":"12121212",
            "created_by":"1",
        },
    },
    {
        "url": "add",
        "info": "try to insert new row with wrong parameters",
        "method": "post",
        "data": {
            "s": "121212",
            "i":"1",
            "desc":"updated description",
            "software":"updated",
            "firmware":"updated",
            "stat":"1",
            "comm":"updated comment",
            "sim":"0101",
            "created_by":"1",
        },
    },
    {
        "url": "update/121212",
        "info": "update the first register",
        "method": "post",
        "data": {
            "serial": "121212",
            "imei":"1",
            "description":"updated description",
            "software_version":"updated",
            "firmware_version":"updated",
            "status":"1",
            "comments":"updated comment",
            "sim_telephone":"12121212",
            "updated_by":"1",
        },
    },
    {
        "url": "update/",
        "info": "try to update without serial",
        "method": "post",
        "data": {
            "serial": "121212",
            "imei":"1",
            "description":"updated description",
            "software_version":"updated",
            "firmware_version":"updated",
            "status":"1",
            "comments":"updated comment",
            "sim_telephone":"12121212",
            "updated_by":"1",
        },
    },
    {
        "url": "update/100000000",
        "info": "try to update with wrong serial",
        "method": "post",
        "data": {
            "serial": "121212",
            "imei":"1",
            "description":"updated description",
            "software_version":"updated",
            "firmware_version":"updated",
            "status":"1",
            "comments":"updated comment",
            "sim_telephone":"12121212",
            "updated_by":"1",
        },
    },
    {
        "url": "update/121212",
        "info": "try to update with wrong parameters",
        "method": "post",
        "data": {
            "s": "121212",
            "i":"1",
            "desc":"updated description",
            "software":"updated",
            "firmware":"updated",
            "stat":"1",
            "comm":"updated comment",
            "sim":"0101",
            "updated_by":"1",
        },
    },
    {
        "url": "update/121212",
        "info": "try to update without 'updated_by' parameter",
        "method": "post",
        "data": {
            "serial": "121212",
            "imei":"1",
            "description":"updated description",
            "software_version":"updated",
            "firmware_version":"updated",
            "status":"1",
            "comments":"updated comment",
            "sim_telephone":"12121212",
        },
    },
]

if __name__ == "__main__":
    test_sim = ApiTest (endpoints_base, endpoints)
    test_sim.run_tests ()