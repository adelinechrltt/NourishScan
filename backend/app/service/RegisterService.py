from app import Session
from app.models.users import User
from app.service.UserService import UserService

  
def register(self, username, password, email) :
    newuser = User(self.username, self.email, self.password, None, None)
    userservice = UserService()

    if not userservice.get_by_email(self.email) :
        self.save(newuser=newuser)
    else :
        return False
        
def save(self,newuser):
        
    with Session() as session :
        session.add(newuser)
        session.commit()
        print("Register Success")