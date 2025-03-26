import models

def validate_user_data(login, password, confirm_password):
    if len(login) > 255:
        raise Exception('Login too long')
    if len(password) > 80:
        raise Exception('Password too long')
    if len(password) < 8:
        raise Exception('Password too short')
    if password != confirm_password:
        raise Exception('Passwords do not match')
    return True

def validate_user(login, password):
    u1 = models.User.load_user_by_username(login)
    if u1.login != login or u1.password != password:
        return False
    return True