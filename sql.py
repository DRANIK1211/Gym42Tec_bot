import sqlite3 as sql

con = sql.connect("base.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    role TEXT NOT NULL
) ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    room TEXT NOT NULL,
    description TEXT NOT NULL,
    department TEXT NOT NULL,
    date TEXT NOT NULL,
    status TEXT NOT NULL
)''')


def register(user_id, username, role):
    cursor.execute(f'''INSERT INTO user (id, username, role) VALUES (?, ?, ?)''',
                   (user_id, username, role))
    con.commit()


def delete(user_id):
    cursor.execute(f'''DELETE FROM user WHERE {user_id}''')
    con.commit()


def search(user_id):
    return cursor.execute(f"SELECT * FROM user WHERE id = ?", (user_id,)).fetchall()


def getname(user_id):
    return cursor.execute(f"SELECT username FROM user WHERE id = ? AND role = ?", (user_id, "User")).fetchall()


def send_application(username, cab, opis, otdel, date):
    st = "Отправлена"
    leng = len(cursor.execute("SELECT * FROM applications").fetchall())
    cursor.execute(f'''INSERT INTO applications (id, username, room, description, department, date, status)
     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (leng, username, cab, opis, otdel, date, st))
    con.commit()
    return leng


def get_otdel(otdel):
    return cursor.execute(f"SELECT id FROM user WHERE role = ?", (otdel,)).fetchall()


def delete_application_user(num):
    cursor.execute(f"DELETE FROM applications WHERE id = ?", (num,))
    con.commit()


def get_application(id):
    a = cursor.execute(f"SELECT username FROM user WHERE id = ?", (id,)).fetchall()[0][0]
    return cursor.execute(f"SELECT * FROM applications WHERE username = ? AND status IN (?, ?)",
                          (a, "Отправлена", "Выполняется")).fetchall()


def get_otdel_tec(id):
    return cursor.execute(f"SELECT role FROM user WHERE {id}").fetchall()


def get_application_tec(otdel):
    #  Исправить просмотр заявок, выходили только "Отправлена", нужно добавить в вывод "Выполняется"
    mas = cursor.execute("SELECT * FROM applications WHERE department = ? AND status IN (?, ?)",
                        (otdel, "Отправлена", "Выполняется")).fetchall()
    return mas


def select(num):
    cursor.execute("UPDATE applications SET status = ? WHERE id = ?", ("Выполняется", num))
    con.commit()


def ok_application(num):
    cursor.execute("UPDATE applications SET status = ? WHERE id = ?", ("Выполнена", num))
    con.commit()


def get_id(num):
    f = cursor.execute("SELECT username FROM applications WHERE id = ?", (num,)).fetchall()
    return cursor.execute(f"SELECT id FROM user WHERE username = ?", (f[0][0],)).fetchall()


con.commit()
