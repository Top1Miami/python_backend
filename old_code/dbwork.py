import sqlite3
from sqlite3 import Error

DEMO_LAUNCH_NUMBER = 5


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def close_connection(connection):
    connection.close()
    print("Connection closed successfully")


def init_table(connection):
    cursor = connection.cursor()
    with open('../sql_script.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()
    cursor.executescript(sql_script)
    print("Script loaded successfully")
    cursor.close()


def add_user(connection, user_id, name, email, is_demo):
    cursor = connection.cursor()
    if is_demo:
        cursor.execute("""INSERT INTO users
							(user_id, name, email, is_demo, launch_left)  
							VALUES (?, ?, ?, ?, ?)""", (user_id, name, email, 1, DEMO_LAUNCH_NUMBER))
    else:
        cursor.execute("""INSERT INTO users
							(user_id, name, email, is_demo, launch_left)  
							VALUES (?, ?, ?, ?, ?)""", (user_id, name, email, 0, DEMO_LAUNCH_NUMBER))
    connection.commit()
    print(f"Query committed")
    cursor.close()


def remove_user(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM users WHERE user_id = ?""", (user_id,))
    connection.commit()
    print(f"Query committed")
    cursor.close()


def get_all_users(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users""")
    total_rows = cursor.fetchall()
    cursor.close()
    return total_rows


def get_user(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users where user_id = ?""", (user_id,))
    total_rows = cursor.fetchone()
    cursor.close()
    return total_rows


def set_demo(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("""UPDATE users set is_demo = ? where user_id = ?""", (1, user_id))
    connection.commit()
    print(f"Query committed")
    cursor.close()


def minus_launch(connection, user_id):
    prev_launch = get_user(connection, user_id)
    if (prev_launch[3] == 0):
        return False
    prev_number = prev_launch[4]
    cursor = connection.cursor()
    cursor.execute("""UPDATE users set launch_left = ? where user_id = ?""", (prev_number - 1, user_id))
    connection.commit()
    print(f"Query committed")
    cursor.close()
