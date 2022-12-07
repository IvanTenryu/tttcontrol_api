import json
from flask import Blueprint, request
from models.installation import Installation
from models.user import User
from sqlalchemy import select
from sqlalchemy import update
from utils.database import get_db_session

# Create blueprint
blueprint_installation = Blueprint ('installation', __name__)

@blueprint_installation.route ("/", methods=["GET", "POST"])
def installation_index ():
    """ show list of endpoints """
    endpoints = {
        "/query": {
            "desciption": "(get) Show all registers in database table"
        },
        "/query/<id>": {
            "desciption": "(get) Show the specific register who match with the id",
            "url paramaters": {
                "id": "(int) id number of the installation"
            }
        },
        "/add/": {
            "desciption": "(post) Insert a new register",
            "json paramaters": {
                "user_id": "int",
                "date": "timestamp",
                "vehicle_description": "str",
                "economic_number": "str",
                "plate": "str",
                "gps_tag": "str",
                "fuse_status": "str",
                "installation_energy_type": "str",
                "ignition_control": "int",
                "ignition_detection": "int",
                "odometer": "int",
                "extra_control": "str",
                "user_validator": "str",
                "created_by": "str"
            }
        },
        "/update/<id>": {
            "desciption": "(post) Update specific register",
            "url paramaters": {
                "id": "(int) id number of the installation"
            },
            "json paramaters": {
                "user_id": "int (optional)",
                "date": "timestamp (optional)",
                "vehicle_description": "str (optional)",
                "economic_number": "str (optional)",
                "plate": "str (optional)",
                "gps_tag": "str (optional)",
                "fuse_status": "str (optional)",
                "installation_energy_type": "str (optional)",
                "ignition_control": "int (optional)",
                "ignition_detection": "int (optional)",
                "odometer": "int (optional)",
                "extra_control": "str (optional)",
                "user_validator": "str (optional)",
                "updated_by": "str"
            }
        },
    }

    return endpoints

@blueprint_installation.route ("/query/", methods=["GET"])
def installation_query ():
    """ return registers from 'installation' table in database """
    
    # get registers from database
    query = select (Installation)
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
            "id": register.id,
            "user_id": register.user_id,
            "date": register.date,
            "vehicle_description": register.vehicle_description,
            "economic_number": register.economic_number,
            "plate": register.plate,
            "gps_tag": register.gps_tag,
            "fuse_status": register.fuse_status,
            "installation_energy_type": register.installation_energy_type,
            "ignition_control": register.ignition_control,
            "ignition_detection": register.ignition_detection,
            "odometer": register.odometer,
            "extra_control": register.extra_control,
            "user_validator": register.user_validator,
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

@blueprint_installation.route ("/query/<int:id>", methods=["GET"])
def installation_query_id (id):
    """ return registers from 'installation' table in database """
    
    # get registers from database
    query = select (Installation).where(Installation.id == id)
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
            "id": register.id,
            "user_id": register.user_id,
            "date": register.date,
            "vehicle_description": register.vehicle_description,
            "economic_number": register.economic_number,
            "plate": register.plate,
            "gps_tag": register.gps_tag,
            "fuse_status": register.fuse_status,
            "installation_energy_type": register.installation_energy_type,
            "ignition_control": register.ignition_control,
            "ignition_detection": register.ignition_detection,
            "odometer": register.odometer,
            "extra_control": register.extra_control,
            "user_validator": register.user_validator,
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

@blueprint_installation.route ("/add/", methods=["POST"])
def installation_add ():

    """ Insert new register in table, with posts requests """

    # Get data from json
    json_data = request.json
    if type(json_data) == str:
        json_data = json.loads(json_data)
    
    # Validate json parameters
    parameters = [
        "user_id", 
        "date", 
        "vehicle_description", 
        "economic_number", 
        "plate",
        "gps_tag",
        "fuse_status",
        "installation_energy_type",
        "ignition_control",
        "ignition_detection",
        "odometer",
        "extra_control",
        "user_validator",
        "created_by"        
    ]
    parameters_ok = True
    for parameter in parameters:
        if parameter not in json_data:
            parameters_ok = False
            break

    if parameters_ok:
        # Save in database
        newInstallation = Installation (
            user_id=json_data["user_id"],
            date=json_data["date"],
            vehicle_description=json_data["vehicle_description"],
            economic_number=json_data["economic_number"],
            plate=json_data["plate"],
            gps_tag=json_data["gps_tag"],
            fuse_status=json_data["fuse_status"],
            installation_energy_type=json_data["installation_energy_type"],
            ignition_control=json_data["ignition_control"],
            ignition_detection=json_data["ignition_detection"],
            odometer=json_data["odometer"],
            extra_control=json_data["extra_control"],
            user_validator=json_data["user_validator"],
            created_by=json_data["created_by"],
        )
        session = get_db_session ()
        session.add (newInstallation)
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

@blueprint_installation.route ("/update/<int:id>", methods=["POST"])
def installation_update (id):

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
    query = select (Installation).where(Installation.id == id)
    session = get_db_session ()
    installations = session.scalars (query).all()

    try:
        installation = installations[0]
    except Exception as e:
        print (e)
        installation = None

    # Return error_: user not found
    if not installation:
        return {
            "status": "error",
            "details": f"installation with the id {id}, not found"
        }, 400

    
    # Validate json parameters
    parameters = [
        "user_id", 
        "date", 
        "vehicle_description", 
        "economic_number", 
        "plate",
        "gps_tag",
        "fuse_status",
        "installation_energy_type",
        "ignition_control",
        "ignition_detection",
        "odometer",
        "extra_control",
        "user_validator",
        "updated_by"
    ]
    paremeters_found = {}
    for key, value in json_data.items():
        if key in parameters:
            paremeters_found[key] = value

    if len(paremeters_found) > 1:

        # update data
        print ("----------------------")
        
        # update data
        query = (
            update(Installation).
            where(Installation.id == id).
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


