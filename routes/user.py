import json
from flask import Blueprint, request
from models.user import User
from sqlalchemy import select
from sqlalchemy import update
from utils.database import get_db_session

# Create blueprint
blueprint_user = Blueprint ('user', __name__)

@blueprint_user.route ("/", methods=["GET", "POST"])
def user_index ():
    """ show list of endpoints """
    endpoints = {
        "/query": {
            "desciption": "(get) Show all registers in database table"
        },
        "/query/<id>": {
            "desciption": "(get) Show the specific register who match with the id",
            "url paramaters": {
                "id": "(int) id number of the user"
            }
        },
        "/add/": {
            "desciption": "(post) Insert a new register",
            "json paramaters": {
                "name": "str",
                "login": "str",
                "password": "str",
                "user_type": "int",
                "status": "int",
                "created_by": "int",
            }
        },
        "/update/<id>": {
            "desciption": "(post) Update specific register",
            "url paramaters": {
                "id": "(int) id number of the user to update"
            },
            "json paramaters": {
                "name": "str (optional)",
                "login": "str (optional)",
                "password": "str (optional)",
                "user_type": "int (optional)",
                "status": "int (optional)",
                "updated_by": "int",
            }
        },
    }

    return endpoints

@blueprint_user.route ("/query/", methods=["GET"])
def user_query ():
    """ return registers from 'users' table in database """

    # get registers from database
    query = select (User)
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
            "name": register.name,
            "login": register.login,
            "password": register.password,
            "user_type": register.user_type,
            "status": register.status,
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

@blueprint_user.route ("/query/<int:id>", methods=["GET"])
def user_query_id (id):
    """ return specific user from 'users' table in database """

    # get registers from database
    query = select (User).where(User.id == id)
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
            "name": register.name,
            "login": register.login,
            "password": register.password,
            "user_type": register.user_type,
            "status": register.status,
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

@blueprint_user.route ("/add/", methods=["POST"])
def user_add ():

    """ Insert new register in table, with posts requests """

    # Get data from json
    json_data = request.json
    if type(json_data) == str:
        json_data = json.loads(json_data)
    
    # Validate json parameters
    parameters = [
        "name", 
        "login", 
        "password", 
        "user_type", 
        "status",
        "created_by"
    ]
    parameters_ok = True
    for parameter in parameters:
        if parameter not in json_data:
            parameters_ok = False
            break

    if parameters_ok:
        # Save in database
        newUser = User (
            name=json_data["name"],
            login=json_data["login"],
            password = json_data["password"],
            user_type = json_data["user_type"],
            status = json_data["status"],
            created_by = json_data["created_by"],
        )
        session = get_db_session ()
        session.add (newUser)
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

@blueprint_user.route ("/update/<int:id>", methods=["POST"])
def user_update (id):

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
    query = select (User).where(User.id == id)
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
            "details": f"user with the id {id}, not found"
        }, 400

    
    # Validate json parameters
    parameters = [
        "name", 
        "login", 
        "password", 
        "user_type", 
        "status",
        "updated_by"
    ]
    paremeters_found = {}
    for key, value in json_data.items():
        if key in parameters:
            paremeters_found[key] = value


    if len(paremeters_found) > 1:

        # update data
        query = (
            update(User).
            where(User.id == id).
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

