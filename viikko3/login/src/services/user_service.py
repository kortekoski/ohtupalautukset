from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user
    
    def username_in_use(self, username):
            if self._user_repository.find_by_username(username) is None:
                return False
            return True

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if type(username) is not str or type(password) is not str:
            raise AuthenticationError("Invalid type of username or password")
        
        if len(username) < 3:
            raise AuthenticationError("The username must be at least 3 characters long.")
        
        if len(password) < 8:
            raise AuthenticationError("The password must be at least 8 characters long.")
        
        if password.isalpha():
            raise AuthenticationError("The password must include at least one non-letter character.")
        
        if password != password_confirmation:
            raise AuthenticationError("Incorrect password confirmation")
        
        if self.username_in_use(username):
            raise AuthenticationError("Username already in use")

user_service = UserService()
