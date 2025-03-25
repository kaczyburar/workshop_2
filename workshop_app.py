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



if __name__ == '__main__':
    app.run(debug=True)

