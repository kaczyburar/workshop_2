from sql_utilis import execute_sql
import datetime

class User:
    def __init__(self,login,password, confirm_password):
        self.login = login
        self.password = password
        self.confirm_password = confirm_password
        self.id = None

    def __str__(self):
        return f'{self.login} {self.password}'

    def save(self, password = None):
        if self.id is None:
            sql = "INSERT INTO users (login, password, confirm_password) VALUES (%s, %s, %s) returning id"
            ret_val = execute_sql(sql,'workshop', self.login, self.password, self.confirm_password)[0]
            self.id = ret_val
        else:
            sql = "UPDATE users SET password = %s WHERE id = %s"
            sql2 = "UPDATE users SET confirm_password = %s WHERE id = %s"
            ret_val = execute_sql(sql, 'workshop', password, self.id)
            ret_val2 = execute_sql(sql2, 'workshop', password, self.id)
            self.password = password
            self.confirm_password = password
            return True

    @classmethod
    def load_user_by_username(cls, login):
        sql = "SELECT * FROM users WHERE login = %s"
        ret_val = execute_sql(sql, 'workshop', login)
        if ret_val is not None:
            for row in ret_val:
                u = cls(row[1], row[2], row[3])
                u.id = row[0]
            return u
        return None
    @classmethod
    def load_user_by_id(cls, id):
        sql = "SELECT * FROM users WHERE id = %s"
        try:
            ret_val = execute_sql(sql, 'workshop', id)[0]
            u = cls(ret_val[1], ret_val[2], ret_val[3])
            u.id = ret_val[0]
            return u
        except IndexError:
            return None

    @classmethod
    def load_all_users(cls):
        sql = "SELECT * FROM users"
        ret_val = execute_sql(sql, 'workshop')
        logins = [login[1] for login in ret_val]
        # users = []
        # for u in ret_val:
        #     u = cls(u[1], u[2], u[3])
        #     u.id = ret_val[0]
        #     users.append(u)
        # return users
        return logins

    def delete(self):
        if self.id is not None:
            sql = "DELETE FROM users WHERE id = %s"
            ret_val = execute_sql(sql, 'workshop', self.id)
            self.id = None
            return True
        else:
            return False


class Message:
    def __init__(self, from_id, to_id, text):
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self._id = None
        self._creation_date = None

    @property
    def id(self):
        return self._id

    def save(self, text = None):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        if self._id is None:
            sql = "INSERT INTO messages (from_id, to_id, creation_date, text) VALUES (%s, %s, %s, %s) returning id"
            ret_val = execute_sql(sql, 'workshop', self.from_id, self.to_id, date, self.text)[0]
            self._id = ret_val[0]
        else:
            sql = "UPDATE messages SET creation_date = %s, text = %s WHERE id = %s"
            execute_sql(sql, 'workshop', date, text, self._id)
        return self

    @staticmethod
    def load_all_messages():
        sql = "SELECT * FROM messages"
        ret_val = execute_sql(sql, 'workshop')
        return ret_val

    @staticmethod
    def load_message(id):
        sql = "SELECT * FROM messages WHERE id = %s"
        ret_val = execute_sql(sql, 'workshop', id)[0]
        return ret_val

    @staticmethod
    def delete_message(id):
        sql = "DELETE FROM messages WHERE id = %s"
        ret_val = execute_sql(sql, 'workshop', id)
        return f"Poprawnie usunieto wiadomosc o id {id}"
