from app.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import text


class UserRepository:
    def __init__(self,db:Session):
        self.db = db
    
    # query the database and fetch all the users available.   
    def get_all_users(self) -> list[User]:
        return self.db.query(User).all()
    
   # Get user by email.
    def get_user_by_email(self, email:str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    # Creates new user.    
    def create_user(self, user:User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
        
    # # Saves the changes after the emp id is created.    
    # def save_user_changes(self, user:User) -> User:       
    #     self.db.commit()
    #     self.db.refresh(user)
    #     return user

    # get the next sequence of emp id from the db.
    def get_next_emp_sequence(self) -> int:
        result = self.db.execute(text("select nextval('employee_id_seq')"))
        return result.scalar_one()


