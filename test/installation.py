import datetime
from base import ApiTest

# Endpoints data for tests
endpoints_base = "installation"
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
            "user_id": 1,
            "date": datetime.datetime.now(),
            "vehicle_description": "sample description",
            "economic_number": "sample num",
            "plate": "sample plate",
            "gps_tag": "sample tag",
            "fuse_status": "sample fuse",
            "installation_energy_type": "sample",
            "ignition_control": 1,
            "ignition_detection": 1,
            "odometer": 1,
            "extra_control": "sample extra",
            "user_validator": "sample validation",
            "created_by": 1,
        },
    },
    {
        "url": "add",
        "info": "try to insert new row with wrong parameters",
        "method": "post",
        "data": {
            "user": 1,
            "d": datetime.datetime.now(),
            "vehicle": "sample description",
            "economic": "sample num",
            "p": "sample plate",
            "gps": "sample tag",
            "fuse": "sample fuse",
            "installation": "sample",
            "ignition": 1,
            "odom": 1,
            "extra": "sample extra",
            "user": "sample validation",
            "created_by": 1,
        },
    },
    {
        "url": "update/1",
        "info": "update the first register",
        "method": "post",
        "data": {
            "user_id": 1,
            "date": datetime.datetime.now(),
            "vehicle_description": "updated description",
            "economic_number": "sample num",
            "plate": "sample plate",
            "gps_tag": "sample tag",
            "fuse_status": "sample fuse",
            "installation_energy_type": "sample",
            "ignition_control": 1,
            "ignition_detection": 1,
            "odometer": 1,
            "extra_control": "sample extra",
            "user_validator": "sample validation",
            "updated_by": 1,
        },
    },
    {
        "url": "update/",
        "info": "try to update without id",
        "method": "post",
        "data": {
            "user_id": 1,
            "date": datetime.datetime.now(),
            "vehicle_description": "updated description",
            "economic_number": "sample num",
            "plate": "sample plate",
            "gps_tag": "sample tag",
            "fuse_status": "sample fuse",
            "installation_energy_type": "sample",
            "ignition_control": 1,
            "ignition_detection": 1,
            "odometer": 1,
            "extra_control": "sample extra",
            "user_validator": "sample validation",
            "updated_by": 1,
        },
    },
    {
        "url": "update/9999",
        "info": "try to update with wrong id",
        "method": "post",
        "data": {
            "user_id": 1,
            "date": datetime.datetime.now(),
            "vehicle_description": "updated description",
            "economic_number": "sample num",
            "plate": "sample plate",
            "gps_tag": "sample tag",
            "fuse_status": "sample fuse",
            "installation_energy_type": "sample",
            "ignition_control": 1,
            "ignition_detection": 1,
            "odometer": 1,
            "extra_control": "sample extra",
            "user_validator": "sample validation",
            "updated_by": 1,
        },
    },
    {
        "url": "update/1",
        "info": "try to update with wrong parameters",
        "method": "post",
        "data": {
            "user": 1,
            "d": datetime.datetime.now(),
            "vehicle": "updated description",
            "economic": "sample num",
            "p": "sample plate",
            "gps": "sample tag",
            "fuse": "sample fuse",
            "installation": "sample",
            "ignition": 1,
            "odom": 1,
            "extra": "sample extra",
            "user": "sample validation",
            "updated_by": 1,
        },
    },
    {
        "url": "update/1",
        "info": "try to update without 'updated_by' parameter",
        "method": "post",
        "data": {
            "user_id": 1,
            "date": datetime.datetime.now(),
            "vehicle_description": "updated description",
            "economic_number": "sample num",
            "plate": "sample plate",
            "gps_tag": "sample tag",
            "fuse_status": "sample fuse",
            "installation_energy_type": "sample",
            "ignition_control": 1,
            "ignition_detection": 1,
            "odometer": 1,
            "extra_control": "sample extra",
            "user_validator": "sample validation",
        },
    },
]

if __name__ == "__main__":
    test_installation = ApiTest (endpoints_base, endpoints)
    test_installation.run_tests ()