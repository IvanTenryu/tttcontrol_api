import datetime
from base import ApiTest

# Endpoints data for tests
endpoints_base = "maintenance"
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
            "date": datetime.datetime.now(),
            "economic_number": "sample num",
            "issue_description": "sample issue",
            "gps_tag": "sample tag",
            "fuse_status": "sample status",
            "installation_energy_type": "sample",
            "installation_status": "sample",
            "switch": "gps",
            "new_tag": "sample new tag",
            "user_validator": "sample validator",
            "user_id": 1,
            "created_by": 1
        },
    },
    {
        "url": "add",
        "info": "try to insert new row with wrong parameters",
        "method": "post",
        "data": {
            "date": datetime.datetime.now(),
            "economic": "sample num",
            "issue": "sample issue",
            "gps": "sample tag",
            "fuse": "sample status",
            "installation": "sample",
            "installation": "sample",
            "switch": "gps",
            "new": "sample new tag",
            "user": "sample validator",
        },
    },
    {
        "url": "update/1",
        "info": "update the first register",
        "method": "post",
        "data": {
            "date": datetime.datetime.now(),
            "economic_number": "updated num",
            "issue_description": "updated issue",
            "gps_tag": "updated tag",
            "fuse_status": "updated status",
            "installation_energy_type": "updated",
            "installation_status": "updated",
            "switch": "gps",
            "new_tag": "updated new tag",
            "user_validator": "updated validator",
            "user_id": 1,
            "updated_by": 1
        },
    },
    {
        "url": "update/",
        "info": "try to update without id",
        "method": "post",
        "data": {
            "date": datetime.datetime.now(),
            "economic_number": "updated num",
            "issue_description": "updated issue",
            "gps_tag": "updated tag",
            "fuse_status": "updated status",
            "installation_energy_type": "updated",
            "installation_status": "updated",
            "switch": "gps",
            "new_tag": "updated new tag",
            "user_validator": "updated validator",
            "user_id": 1,
            "updated_by": 1
        },
    },
    {
        "url": "update/9999",
        "info": "try to update with wrong id",
        "method": "post",
        "data": {
            "date": datetime.datetime.now(),
            "economic_number": "updated num",
            "issue_description": "updated issue",
            "gps_tag": "updated tag",
            "fuse_status": "updated status",
            "installation_energy_type": "updated",
            "installation_status": "updated",
            "switch": "gps",
            "new_tag": "updated new tag",
            "user_validator": "updated validator",
            "user_id": 1,
            "updated_by": 1
        },
    },
    {
        "url": "update/1",
        "info": "try to update with wrong parameters",
        "method": "post",
        "data": {
            "d": datetime.datetime.now(),
            "economic": "updated num",
            "issue": "updated issue",
            "gps": "updated tag",
            "fuse": "updated status",
            "installation": "updated",
            "s": "gps",
            "new": "updated new tag",
            "user": "updated validator",
            "updated_by": 1
        },
    },
    {
        "url": "update/1",
        "info": "try to update without 'updated_by' parameter",
        "method": "post",
        "data": {
            "date": datetime.datetime.now(),
            "economic_number": "updated num",
            "issue_description": "updated issue",
            "gps_tag": "updated tag",
            "fuse_status": "updated status",
            "installation_energy_type": "updated",
            "installation_status": "updated",
            "switch": "gps",
            "new_tag": "updated new tag",
            "user_validator": "updated validator",
            "user_id": 1,
        },
    },
    {
        "url": "update/1",
        "info": "try to update with wrong switch",
        "method": "post",
        "data": {
            "date": datetime.datetime.now(),
            "economic_number": "updated num",
            "issue_description": "updated issue",
            "gps_tag": "updated tag",
            "fuse_status": "updated status",
            "installation_energy_type": "updated",
            "installation_status": "updated",
            "switch": "wrong switch",
            "new_tag": "updated new tag",
            "user_validator": "updated validator",
            "user_id": 1,
            "updated_by": 1
        },
    },
]

if __name__ == "__main__":
    test_maintenance = ApiTest (endpoints_base, endpoints)
    test_maintenance.run_tests ()