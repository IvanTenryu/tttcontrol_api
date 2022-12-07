import json
from flask import Blueprint, request
from models.sim import Sim
from sqlalchemy import select
from sqlalchemy import update
from utils.database import get_db_session

# Create blueprint
blueprint_sim = Blueprint ('sim', __name__)

@blueprint_sim.route ("/", methods=["GET", "POST"])
def sim_index ():
    
    """ show list of endpoints """
    endpoints = {
        "/query": {
            "desciption": "(get) Show all registers in database table"
        },
        "/query/<telephone>": {
            "desciption": "(get) Show the specific register who match with the id",
            "url paramaters": {
                "telephone": "(int) telephone number of the sim"
            }
        },
        "/add/": {
            "desciption": "(post) Insert a new register",
            "json paramaters": {
                "telephone": "int",
                "account": "str",
                "father_account": "str",
                "iccid": "str",
                "package": "str",
                "status": "int",
                "created_by": "int"
            }
        },
        "/update/<telephone>": {
            "desciption": "(post) Update specific register",
            "url paramaters": {
                "telephone": "(int) telephone number of the sim"
            },
            "json paramaters": {
                "telephone": "int (optional)",
                "account": "str (optional)",
                "father_account": "str (optional)",
                "iccid": "str (optional)",
                "package": "str (optional)",
                "status": "int (optional)",
                "cancellation_date": "timestamp (optional)",
                "updated_by": "int"
            }
        },
    }

    return endpoints

@blueprint_sim.route ("/query/", methods=["GET"])
def sim_query ():
    """ return registers from 'sim' table in database """
    
    # get registers from database
    query = select (Sim)
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
            "telephone": register.telephone,
            "account": register.account,
            "father_account": register.father_account,
            "iccid": register.iccid,
            "package": register.package,
            "status": register.status,
            "cancellation_date": register.cancellation_date,
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

@blueprint_sim.route ("/query/<int:telephone>", methods=["GET"])
def sim_query_telephone (telephone):
    """ return specific sim from 'sim' table in database """
    
    # get registers from database
    query = select (Sim).where(Sim.telephone == telephone)
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
            "telephone": register.telephone,
            "account": register.account,
            "father_account": register.father_account,
            "iccid": register.iccid,
            "package": register.package,
            "status": register.status,
            "cancellation_date": register.cancellation_date,
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

@blueprint_sim.route ("/add/", methods=["POST"])
def sim_add ():

    """ Insert new register in table, with posts requests """

    # Get data from json
    json_data = request.json
    if type(json_data) == str:
        json_data = json.loads(json_data)
    
    # Validate json parameters
    parameters = [
        "telephone",
        "account",
        "father_account",
        "iccid",
        "package",
        "status",
        "created_by",
    ]
    parameters_ok = True
    for parameter in parameters:
        if parameter not in json_data:
            parameters_ok = False
            break

    if parameters_ok:

        # Validate if the telefone already exists
        telephone = json_data["telephone"]
        query = select (Sim).where(Sim.telephone == telephone)
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
                "details": f"sim with the telephone {telephone}, already exists"
            }, 400

        # Save in database
        newSim = Sim (
            telephone=json_data["telephone"],
            account=json_data["account"],
            father_account = json_data["father_account"],
            iccid = json_data["iccid"],
            package = json_data["package"],
            status = json_data["status"],
            created_by = json_data["created_by"]
        )
        session = get_db_session ()
        session.add (newSim)
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

@blueprint_sim.route ("/update/<int:telephone>", methods=["POST"])
def sim_update (telephone):

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
    query = select (Sim).where(Sim.telephone == telephone)
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
            "details": f"user with the telephone {telephone}, not found"
        }, 400

    
    # Validate json parameters
    parameters = [
        "telephone",
        "account",
        "father_account",
        "iccid",
        "package",
        "status",
        "cancellation_date",
    ]
    paremeters_found = {}
    for key, value in json_data.items():
        if key in parameters:
            paremeters_found[key] = value


    if len(paremeters_found) > 1:

        # update data
        query = (
            update(Sim).
            where(Sim.telephone == telephone).
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
