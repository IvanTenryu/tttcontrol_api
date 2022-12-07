import json
from flask import Blueprint, request
from models.change_log import ChangeLog
from sqlalchemy import select
from sqlalchemy import update
from utils.database import get_db_session

# Create blueprint
blueprint_change_log = Blueprint ('change_log', __name__)

@blueprint_change_log.route ("/", methods=["GET", "POST"])
def change_log_index ():
    """ show list of endpoints """
    endpoints = {
        "/query": {
            "desciption": "(get) Show all registers in database table"
        },
        "/query/<id>": {
            "desciption": "(get) Show the specific register who match with the id",
            "url paramaters": {
                "id": "(int) id number of the log"
            }
        },
        "/add/": {
            "desciption": "(post) Insert a new register",
            "json paramaters": {
                "gps_serial": "int",
                "date": "timestamp",
                "type": "str",
                "previous_value": "int",
                "new_value": "int",
            }
        },
        "/update/<id>": {
            "desciption": "(post) Update specific register",
            "url paramaters": {
                "id": "(int) id number of the user to update"
            },
            "json paramaters": {
                "gps_serial": "int (optional)",
                "date": "timestamp (optional)",
                "type": "str (optional)",
                "previous_value": "int (optional)",
                "new_value": "int (optional)",
            }
        }
    }

    return endpoints

@blueprint_change_log.route ("/query/", methods=["GET"])
def change_log_query ():
    """ return registers from 'change_log' table in database """
    
    # get registers from database
    query = select (ChangeLog)
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
            "gps_serial": register.gps_serial,
            "date": register.date,
            "type": register.type,
            "previous_value": register.previous_value,
            "new_value": register.new_value
        })

    # Update max numbers of registers
    registers_formated["results_num"] = results_num

    return (registers_formated)

@blueprint_change_log.route ("/query/<int:id>", methods=["GET"])
def change_log_query_id (id):
    """ return specific log from 'change_log' table in database """    
    
    # get registers from database
    query = select (ChangeLog).where(ChangeLog.id == id)
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
            "gps_serial": register.gps_serial,
            "date": register.date,
            "type": register.type,
            "previous_value": register.previous_value,
            "new_value": register.new_value
        })

    # Update max numbers of registers
    registers_formated["results_num"] = results_num

    return registers_formated

@blueprint_change_log.route ("/add/", methods=["POST"])
def change_log_add ():

    """ Insert new register in table, with posts requests """

    # Get data from json
    json_data = request.json
    if type(json_data) == str:
        json_data = json.loads(json_data)
    
    # Validate json parameters
    parameters = [
        "gps_serial", 
        "date", 
        "type", 
        "previous_value", 
        "new_value",
    ]
    parameters_ok = True
    for parameter in parameters:
        if parameter not in json_data:
            parameters_ok = False
            print (parameter)
            break

    if parameters_ok:
        # Save in database
        newChangeLog = ChangeLog (
            gps_serial=json_data["gps_serial"],
            date=json_data["date"],
            type = json_data["type"],
            previous_value = json_data["previous_value"],
            new_value = json_data["new_value"],
        )
        session = get_db_session ()
        session.add (newChangeLog)
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

@blueprint_change_log.route ("/update/<int:id>", methods=["POST"])
def change_log_update (id):

    """ Update specific register in table, with posts requests """

    # Get data from json
    json_data = request.json
    if type(json_data) == str:
        json_data = json.loads(json_data)

    # Get user from database
    query = select (ChangeLog).where(ChangeLog.id == id)
    session = get_db_session ()
    change_logs = session.scalars (query).all()

    try:
        change_log = change_logs[0]
    except Exception as e:
        print (e)
        change_log = None

    # Return error_: user not found
    if not change_log:
        return {
            "status": "error",
            "details": f"log with the id {id}, not found"
        }, 400

    
    # Validate json parameters
    parameters = [
        "gps_serial", 
        "date", 
        "type", 
        "previous_value", 
        "new_value",
    ]
    paremeters_found = {}
    for key, value in json_data.items():
        if key in parameters:
            paremeters_found[key] = value


    if len(paremeters_found) > 0:

        # update data
        query = (
            update(ChangeLog).
            where(ChangeLog.id == id).
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

