import json
from flask import Blueprint, request
from models.gps import Gps
from sqlalchemy import select
from sqlalchemy import update
from utils.database import get_db_session

# Create blueprint
blueprint_gps = Blueprint ('gps', __name__)

@blueprint_gps.route ("/", methods=["GET", "POST"])
def gps_index ():
    """ show list of endpoints """
    endpoints = {
        "/query": {
            "desciption": "(get) Show all registers in database table"
        },
        "/query/<serial>": {
            "desciption": "(get) Show the specific register who match with the id",
            "url paramaters": {
                "serial": "(int) serial number of the gps"
            }
        },
        "/add/": {
            "desciption": "(post) Insert a new register",
            "json paramaters": {
                "serial": "int",
                "imei":"int",
                "description":"str",
                "software_version":"str",
                "firmware_version":"str",
                "status":"int",
                "comments":"str",
                "sim_telephone":"int",
                "created_by":"int",
            }
        },
        "/update/<serial>": {
            "desciption": "(post) Update specific register",
            "url paramaters": {
                "serial": "(int) serial number of the sim"
            },
            "json paramaters": {
                "serial": "int (optional)",
                "imei":"int (optional)",
                "description":"str (optional)",
                "software_version":"str (optional)",
                "firmware_version":"str (optional)",
                "status":"int (optional)",
                "comments":"str (optional)",
                "sim_telephone":"int (optional)",
                "updated_by":"int",
            }
        },
    }

    return endpoints

@blueprint_gps.route ("/query/", methods=["GET"])
def gps_query ():
    """ return registers from 'gps' table in database """
    
    # get registers from database
    query = select (Gps)
    session = get_db_session ()
    registers = session.scalars (query)

    # Format data
    registers_formated = {
        "results_num":  0,
        "registers": []
    }

    results_num = 0
    for register in registers:
        results_num += 1
        registers_formated["registers"].append ({
            "serial": register.serial,
            "imei": register.imei,
            "description": register.description,
            "software_version": register.software_version,
            "firmware_version": register.firmware_version,
            "status": register.status,
            "comments": register.comments,
            "sim_telephone": register.sim_telephone,
            "created_at": register.created_at,
            "updated_at": register.updated_at,
            "deleted_at": register.deleted_at,
            "created_by": register.created_by,
            "updated_by": register.updated_by,
            "deleted_by": register.deleted_by
        })

    # Update max numbers of registers
    registers_formated["results_num"] = results_num

    return (registers_formated)

@blueprint_gps.route ("/query/<int:serial>", methods=["GET"])
def gps_query_serial (serial):
    
    # get registers from database
    query = select (Gps).where(Gps.serial == serial)
    session = get_db_session ()
    registers = session.scalars (query)

    # Format data
    registers_formated = {
        "results_num":  0,
        "registers": []
    }

    results_num = 0
    for register in registers:
        results_num += 1
        registers_formated["registers"].append ({
            "serial": register.serial,
            "imei": register.imei,
            "description": register.description,
            "software_version": register.software_version,
            "firmware_version": register.firmware_version,
            "status": register.status,
            "comments": register.comments,
            "sim_telephone": register.sim_telephone,
            "created_at": register.created_at,
            "updated_at": register.updated_at,
            "deleted_at": register.deleted_at,
            "created_by": register.created_by,
            "updated_by": register.updated_by,
            "deleted_by": register.deleted_by
        })

    # Update max numbers of registers
    registers_formated["results_num"] = results_num

    return registers_formated

@blueprint_gps.route ("/add/", methods=["POST"])
def gps_add ():

    """ Insert new register in table, with posts requests """

    # Get data from json
    json_data = request.json
    if type(json_data) == str:
        json_data = json.loads(json_data)
    
    # Validate json parameters
    parameters = [
        "serial",
        "imei",
        "description",
        "software_version",
        "firmware_version",
        "status",
        "comments",
        "sim_telephone",
        "created_by"
    ]
    parameters_ok = True
    for parameter in parameters:
        if parameter not in json_data:
            parameters_ok = False
            break

    if parameters_ok:

        # Validate if the telefone already exists
        serial = json_data["serial"]
        query = select (Gps).where(Gps.serial == serial)
        session = get_db_session ()
        users = session.scalars (query).all()

        try:
            user = users[0]
        except Exception as e:
            print (e)
            user = None

        # Return error_: user not found
        if user:
            return {
                "status": "error",
                "details": f"gps with the serial {serial}, already exists"
            }, 400

        # Save in database
        newGps = Gps (
            serial=json_data["serial"],
            imei=json_data["imei"],
            description = json_data["description"],
            software_version = json_data["software_version"],
            firmware_version = json_data["firmware_version"],
            status = json_data["status"],
            comments = json_data["comments"],
            sim_telephone = json_data["sim_telephone"],
            created_by = json_data["created_by"]
        )
        session = get_db_session ()
        session.add (newGps)
        session.commit ()
        
        # Confirmation message
        return {
            "status": "done"
        }
    else:
        # return error
        return {
            "status": "error",
            "details": "one or more json parameters not found"
        }, 400

@blueprint_gps.route ("/update/<int:serial>", methods=["POST"])
def gps_update (serial):

    """ Update specific register in table, with posts requests """

    # Get data from json
    json_data = request.json
    if type(json_data) == str:
        json_data = json.loads(json_data)

    # Validate the parameter "updated_by"
    if not "updated_by" in json_data.keys():
        return {
            "status": "error",
            "details": f"'updated_by' its a required parameter"
        }, 400

    # Get user from database
    query = select (Gps).where(Gps.serial == serial)
    session = get_db_session ()
    users = session.scalars (query).all()

    try:
        user = users[0]
    except Exception as e:
        print (e)
        user = None

    # Return error_: user not found
    if not user:
        return {
            "status": "error",
            "details": f"gps with the serial {serial}, not found"
        }, 400

    
    # Validate json parameters
    parameters = [
        "serial",
        "imei",
        "description",
        "software_version",
        "firmware_version",
        "status",
        "comments",
        "sim_telephone",
        "updated_by"
    ]
    paremeters_found = {}
    for key, value in json_data.items():
        if key in parameters:
            paremeters_found[key] = value


    if len(paremeters_found) > 1:

        # update data
        query = (
            update(Gps).
            where(Gps.serial == serial).
            values(paremeters_found)
        )
        session = get_db_session ()
        session.execute (query)
        session.commit ()

        # Confirmation message
        return {
            "status": "done"
        }
    else:
        # Return error
        return {
            "status": "error",
            "details": "one or more json parameters not found"
        }, 400
