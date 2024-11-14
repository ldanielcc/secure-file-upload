from flask_login import UserMixin
import bcrypt

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = str(id)  # Make sure the user ID is always a string
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

# Update users to use strings as IDs
users = {
    "1": User(1, "user1", "password1"),
    "2": User(2, "user2", "password2")
}
