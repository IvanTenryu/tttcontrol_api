import json
from flask import Blueprint, request
from models.maintenance import Maintenance
from sqlalchemy import select
from sqlalchemy import update
from utils.database import get_db_session

# Create blueprint
blueprint_maintenance = Blueprint ('maintenance', __name__)

@blueprint_maintenance.route ("/", methods=["GET", "POST"])
def maintenance_index ():
    """ show list of endpoints """
    endpoints = {
        "/query": {
            "desciption": "(get) Show all registers in database table"
        },
        "/query/<id>": {
            "desciption": "(get) Show the specific register who match with the id",
            "url paramaters": {
                "id": "(int) id number of the maintenance"
            }
        },
        "/add/": {
            "desciption": "(post) Insert a new register",
            "json paramaters": {
                "date": "timestamp",
                "economic_number":"str",
                "issue_description":"str",
                "gps_tag":"str",
                "fuse_status":"str",
                "installation_energy_type":"str",
                "installation_status":"str",
                "switch":"str ['none', 'gps', 'sim']",
                "new_tag":"str",
                "user_validator":"str",
                "user_id":"int",
                "created_by": "int"
            }
        },
        "/update/<id>": {
            "desciption": "(post) Update specific register",
            "url paramaters": {
                "id": "(int) id number of the Maintenance to update"
            },
            "json paramaters": {
                "date": "timestamp (optional)",
                "economic_number":"str (optional)",
                "issue_description":"str (optional)",
                "gps_tag":"str (optional)",
                "fuse_status":"str (optional)",
                "installation_energy_type":"str (optional)",
                "installation_status":"str (optional)",
                "switch":"str ['none', 'gps', 'sim']  (optional)",
                "new_tag":"str (optional)",
                "user_validator":"str (optional)",
                "user_id":"int (optional)",
                "updated_by": "int"
            }
        },
    }

    return endpoints

@blueprint_maintenance.route ("/query/", methods=["GET"])
def maintenance_query ():
    """ return registers from 'maintenance' table in database """

    # get registers from database
    query = select (Maintenance)
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
            "date": register.date,
            "economic_number": register.economic_number,
            "issue_description": register.issue_description,
            "gps_tag": register.gps_tag,
            "fuse_status": register.fuse_status,
            "installation_energy_type": register.installation_energy_type,
            "installation_status": register.installation_status,
            "switch": register.switch,
            "new_tag": register.new_tag,
            "user_validator": register.user_validator,
            "user_id": register.user_id,
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


@blueprint_maintenance.route ("/query/<int:id>", methods=["GET"])
def maintenance_query_id (id):
    """ return specific maintenance from 'maintenance' table in database """    
    
    # get registers from database
    query = select (Maintenance).where(Maintenance.id == id)
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
            "date": register.date,
            "economic_number": register.economic_number,
            "issue_description": register.issue_description,
            "gps_tag": register.gps_tag,
            "fuse_status": register.fuse_status,
            "installation_energy_type": register.installation_energy_type,
            "installation_status": register.installation_status,
            "switch": register.switch,
            "new_tag": register.new_tag,
            "user_validator": register.user_validator,
            "user_id": register.user_id,
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

@blueprint_maintenance.route ("/add/", methods=["POST"])
def maintenance_add ():

    """ Insert new register in table, with posts requests """

    # Get data from json
    json_data = request.json
    if type(json_data) == str:
        json_data = json.loads(json_data)
    
    # Validate json parameters
    parameters = [
        "date", 
        "economic_number", 
        "issue_description", 
        "gps_tag", 
        "fuse_status",
        "installation_energy_type",
        "installation_status",
        "switch",
        "new_tag",
        "user_validator",
        "user_id",
        "created_by",
    ]
    parameters_ok = True
    for parameter in parameters:
        if parameter not in json_data:
            parameters_ok = False
            break

    if parameters_ok:
        # Save in database
        newMaintenance = Maintenance (
            date=json_data["date"],
            economic_number=json_data["economic_number"],
            issue_description=json_data["issue_description"],
            gps_tag=json_data["gps_tag"],
            fuse_status=json_data["fuse_status"],
            installation_energy_type=json_data["installation_energy_type"],
            installation_status=json_data["installation_status"],
            switch=json_data["switch"],
            new_tag=json_data["new_tag"],
            user_validator=json_data["user_validator"],
            user_id=json_data["user_id"],
            created_by=json_data["created_by"],
        )
        session = get_db_session ()
        session.add (newMaintenance)
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

@blueprint_maintenance.route ("/update/<int:id>", methods=["POST"])
def maintenance_update (id):

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

    # Get Maintenance from database
    query = select (Maintenance).where(Maintenance.id == id)
    session = get_db_session ()
    maintenances = session.scalars (query).all()

    try:
        maintenance = maintenances[0]
    except Exception as e:
        print (e)
        maintenance = None

    # Return error: Maintenance not found
    if not maintenance:
        return {
            "status": "error",
            "details": f"maintenance with the id {id}, not found"
        }, 400

    
    # Validate json parameters
    parameters = [
        "date", 
        "economic_number", 
        "issue_description", 
        "gps_tag", 
        "fuse_status",
        "installation_energy_type",
        "installation_status",
        "switch",
        "new_tag",
        "user_validator",
        "user_id",
        "updated_by",
    ]
    paremeters_found = {}
    for key, value in json_data.items():
        if key in parameters:
            paremeters_found[key] = value


    if len(paremeters_found) > 1:

        # Validate switch value
        if "switch" in paremeters_found.keys():
            switch = paremeters_found["switch"]
            siwtch_values = ["none","gps","sim"]
            if switch not in siwtch_values:
                # Return error
                return {
                    "status": "error",
                    "details": f"Invalid value in switch paramter. Onlly allowed: {', '.join(siwtch_values)}"
                }, 400
                        

        # update data
        query = (
            update(Maintenance).
            where(Maintenance.id == id).
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

