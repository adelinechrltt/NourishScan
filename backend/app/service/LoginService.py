
from app.models.users import User
from app.service.UserService import UserService


def __init__(self, username, password):
        self.username = username
        self.password = password
     
    # Return false kalau credential salah, Return class user kalau credential benar
def login(self) :
        userservice = UserService()
        userexists = userservice.get_user(self.username)
   
        if not userexists :
            return False

        if not userservice.check_password(userexists, self.password) :
            return False
    
        return userexists
        