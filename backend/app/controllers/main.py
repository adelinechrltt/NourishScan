from flask import (
    Blueprint, json, jsonify, render_template
)


from app import Base, Session
from app.models.users import User
from app.service.UserService import UserService
from app.service.LoginService import login
from app.service.RegisterService import register
import datetime
from sqlalchemy.sql.expression import FromClause, select


bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    services = UserService()
    # Test Register Service
    
    print("Register Status = " , register("Antony", "password123", "Antony@gmail.uk"))

    # Test Login Service
    Login = login("Antony", "blablabla")
    #Output False
    print("Login Status = " , Login)

    #jsonify
    return jsonify(services.get_all_users())
