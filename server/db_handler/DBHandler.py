from sqlite3 import Error, connect


class DBHandler:
    DEMO_LAUNCH_NUMBER = 5
    PATH = ".\\sm_app.sqlite"
    SCRIPT_PATH = ".\\..\\sql_script.sql"

    def __init__(self):
        self.connection = DBHandler.__create_connection(DBHandler.PATH)
        DBHandler.__init_table(self.connection)

    @staticmethod
    def __create_connection(path):
        connection = None
        try:
            connection = connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    @staticmethod
    def __init_table(connection):
        cursor = connection.cursor()
        with open(DBHandler.SCRIPT_PATH, 'r') as sqlite_file:
            sql_script = sqlite_file.read()
        cursor.executescript(sql_script)
        print("Script loaded successfully")
        cursor.close()

    def add_user(self, user_id, name, email, is_demo):
        cursor = self.connection.cursor()
        if is_demo:
            cursor.execute("""INSERT INTO users
    							(user_id, name, email, is_demo, launch_left)  
    							VALUES (?, ?, ?, ?, ?)""", (user_id, name, email, 1, DBHandler.DEMO_LAUNCH_NUMBER))
        else:
            cursor.execute("""INSERT INTO users
    							(user_id, name, email, is_demo, launch_left)  
    							VALUES (?, ?, ?, ?, ?)""", (user_id, name, email, 0, DBHandler.DEMO_LAUNCH_NUMBER))
        self.connection.commit()
        print(f"Query committed")
        cursor.close()

    def remove_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM users WHERE user_id = ?""", (user_id,))
        self.connection.commit()
        print(f"Query committed")
        cursor.close()

    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT * FROM users""")
        total_rows = cursor.fetchall()
        cursor.close()
        return total_rows

    def get_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT * FROM users where user_id = ?""", (user_id,))
        total_rows = cursor.fetchone()
        cursor.close()
        return total_rows

    def set_demo(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("""UPDATE users set is_demo = ? where user_id = ?""", (1, user_id))
        self.connection.commit()
        print(f"Query committed")
        cursor.close()

    def minus_launch(self, user_id):
        prev_launch = self.get_user(user_id)
        if prev_launch[3] == 1:
            prev_number = prev_launch[4]
            if prev_number == 0:
                return False, "no launches left"
            prev_number = prev_launch[4]
            cursor = self.connection.cursor()
            cursor.execute("""UPDATE users set launch_left = ? where user_id = ?""", (prev_number - 1, user_id))
            self.connection.commit()
            print(f"Query committed")
            cursor.close()
        return True, ""

    def __del__(self):
        DBHandler.__close_connection(self.connection)

    @staticmethod
    def __close_connection(connection):
        connection.close()
        print("Connection closed successfully")
