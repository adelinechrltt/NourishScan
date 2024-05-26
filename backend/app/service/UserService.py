from filecmp import cmp
from app import Base, Session, update
from app.models.users import User

class UserService() :


    session = Session()

    def get_user(self, username) :
        __args__ = self.session.query(User).filter_by(username=username).first()
        return __args__
    
    def get_username(self, username) :
        return self.session.query(User.username).filter_by(username=username)
    
    def check_password(self, userexists, password) :
        user_password = userexists.password
        return password == user_password     
    
    def get_by_email(self, email) :
        return self.session.query(User.email).filter_by(email=email).first()
        
    def update_password(self, email, password) :
        update_args = update(User).where(User.email == email).values(password=password)
        return self.session.execute(update_args)
    
    def update_username(self, email, username) :
        update_args = update(User).where(User.email == email).values(username=username)
        return self.session.execute(update_args)
    
    def update_DOB(self, email, date) :
        update_args = update(User).where(User.email == email).values(DOB=date)
        return self.session.execute(update_args)

    def update_profilepicture(self, email, file) :
        update_args = update(User).where(User.email == email).values(profile_picture=file)
        return None
    
    def update_email(self, email, newemail) :
        update_args = update(User).where(User.email == email).values(email=newemail)
        return self.session.execute(update_args)

    def get_all_users(self) :
        __args__ = (self.session.query(User.__table__.columns).all())
        return [tuple(x) for x in __args__]
    

