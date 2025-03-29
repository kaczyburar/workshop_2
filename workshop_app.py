from flask import Flask, request, render_template
from sql_utilis import execute_sql
import models
import validators
app = Flask(__name__)

@app.route('/create/user', methods=['POST', 'GET'])
def create_user():
    message = None
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if validators.validate_user_data(login, password, confirm_password):
            check_if_uniq_login = models.User.load_user_by_username(login)
            if check_if_uniq_login:
                message = "User already exists"
            else:
                u1 = models.User(login, password, confirm_password)
                u1.save()
                message = "Poprawnie dodano uzytkownika!"
        else:
            message = "Blad podczas dodawnia uzytkowniksa, Sprawdz dane."
        return render_template("create_user.html", message=message)
    else:
        return render_template("create_user.html", message=message)

@app.route('/users', methods=['GET'])
def users():
    users = models.User.load_all_users()
    return render_template("list_users.html", users=users)


@app.route('/send/message', methods=['POST', 'GET'])
def send_message():
    message_ = []
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        rec_username = request.form.get('rec_username')
        message = request.form.get('message')

        validate_user_name_and_passowrd = validators.validate_user(username, password)
        if validate_user_name_and_passowrd:
            check_if_rec_exist = models.User.load_user_by_username(rec_username)
            if check_if_rec_exist:
                user = models.User.load_user_by_username(username)
                rec_user = models.User.load_user_by_username(rec_username)
                m1 = models.Message(user.id, rec_user.id, message)
                m1.save()
            else:
                message_ = "Rec User doesn't exist"
        else:
            message_ = "Bad username or password"
        return render_template("send_message.html", message=message_)
    else:
        return render_template("send_message.html", message=message_)

@app.route('/messages', methods=['POST','GET'])
def messages():
    message_ = []
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if validators.validate_user(login, password):
            u1 = models.User.load_user_by_username(login)
            user_messages = models.Message.load_user_messages(u1.id)
            print(user_messages)
            if user_messages is not None:
                logins = []
                for message in user_messages:
                    u = models.User.load_user_by_id(message[1])
                    logins.append(u.login)
                result = [(mes[0],logins[i], mes[2], mes[3], mes[4]) for i, mes in enumerate(user_messages)]

                return render_template('list_messages.html', usr_mess=result)
            else:
                message_ = "Brak wiadomosci"
                return render_template('login.html', message=message_)
        else:
            message_ = "Bad username or password"
            return render_template('login.html', message=message_)
    else:
        return render_template('login.html', message=message_)

if __name__ == '__main__':
    app.run(debug=True)

