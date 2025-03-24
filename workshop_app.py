from flask import Flask, request, render_template
from sql_utilis import execute_sql
import models
app = Flask(__name__)

@app.route('/create/user', methods=['POST', 'GET'])
def create_user():
    message = None
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if validate_user_data(login, password, confirm_password):
            u1 = models.User(login, password, confirm_password)
            u1.save()
            message = "Poprawnie dodano uzytkownika!"
        else:
            message = "Blad podczas dodawnia uzytkowniksa, Sprawdz dane."
        return render_template("create_user.html", message=message)
    else:
        return render_template("create_user.html", message=message)

def validate_user_data(login, pass1, pass2):
    sql_1 = "SELECT EXISTS(SELECT 1 FROM users WHERE login = %s)"
    result = execute_sql(sql_1, "workshop", login)
    if result[0]:
        return False

    if pass1 != pass2:
        return False
    return True

if __name__ == '__main__':
    app.run(debug=True)

