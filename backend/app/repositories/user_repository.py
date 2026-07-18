from app.models.user import User
from sqlalchemy.orm import Session


class UserRepository:
    # query the database and fetch all the users available.
    @staticmethod
    def get_all_users(db:Session) -> list[User]:
        return db.query(User).all()
    
    @staticmethod
    def get_user_by_email(db:Session, email:str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    # Creates new user.
    @staticmethod
    def create_user(db:Session, user:User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
        
    # Saves the changes after the emp id is created.
    @staticmethod
    def save_user_changes(db:Session, user:User) -> User:       
        db.commit()
        db.refresh(user)
        return user

