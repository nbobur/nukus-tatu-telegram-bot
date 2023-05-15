import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_user(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,   
            Name varchar(124) NOT NULL,
            language varchar(3),
            PRIMARY KEY (id)
            );
            """
        self.execute(sql, commit=True)

    def create_table_hodimlar(self):
        sql = """
        CREATE TABLE Hodimlar(
            id int NOT NULL,
            kalit varchar(24) NOT NULL,
            rasm VARCHAR(1000) NOT NULL,
            info VARCHAR(1000) NOT NULL,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_hodimlar(self, id: int, kalit: str, rasmURL: str, info: str):
        # SQL_EXAMPLE = "INSERT INTO Hodimlar(id, kalit, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Hodimlar(id, kalit, rasm, info) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, kalit, rasmURL, info), commit=True)

    def add_user(self, id: int, name: str, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, language) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)


    def select_all_hodimlar(self):
        sql = """
        SELECT * FROM Hodimlar
        """
        return self.execute(sql, fetchall=True)

    def select_hodimlar(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Hodimlar where id=1 AND Name='John'"
        sql = "SELECT * FROM Hodimlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_kalit(self, kalit):
        sql = f"SELECT * FROM Hodimlar WHERE kalit GLOB '{kalit}';"
        return self.execute(sql, fetchone=True)

    def count_hodimlar(self):
        return self.execute("SELECT COUNT(*) FROM Hodimlar;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Hodimlar SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Hodimlar SET info=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Hodimlar WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
