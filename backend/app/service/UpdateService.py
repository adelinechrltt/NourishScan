import datetime
from app.models.users import User
from app.service.UserService import UserService
class UpdateService :

    def update(self, data) :
        userservice = UserService()

        _new_username = data.get("username")
        _new_password = data.get("password")
        _new_email = data.get("email")
        _new_DOB = data.get("DOB")

        if _new_username :
            userservice.update_username(_new_username)
        
        if _new_password :
            userservice.update_password(_new_password)
        
        if _new_email :
            userservice.update_email(_new_email)

        if _new_DOB :
            userservice.update_DOB(datetime.date(_new_DOB))
