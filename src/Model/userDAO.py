import sqlite3
from src.Model.User import User


def dict_factory(cursor, row):
    """returns each row as a dict, with column names mapped to values

    taken from
    https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory
    """
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

class UserDAO:

    def __init__(self, db_path: str):
        """Create an instance of the UserDAO

        :param db_path: The path to the database containing a Users table
        """
        self.db = db_path
        self.allowed_kwargs = [
            'username',
            'email'
        ]

    def create(self, username: str, password: str, email: str) -> str:
        """Create a new User

        :param username: The username of the user
        :param password: The hashed password of the user
        :param email: The email of the user
        :return: The username of the newly created User if successful, otherwise None
        """
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = 1")  # enables FK constraints
            cur.execute("""
                INSERT INTO Users (
                    username,
                    password,
                    email)
                VALUES (?, ?, ?)
            """, (username, password, email))
            conn.commit()
            return username

    def getUser(self, username: str) -> User:
        """Retrieve the User with the specified username

        :param username: The username of the user to be retrieved
        :return: A User object created with the retrieved data
        """
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            res = cur.execute("""
                SELECT username, email
                FROM Users
                WHERE username = (?)
            """, (username,))
            row = res.fetchone()
            return User(username=row['username'], email=row['email'])

    def update(self, username: str, **kwargs):
        """Update a User

        :param username: The username of the user to be updated
        :param kwargs: The fields to be updated and their new values
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()

            # stmt is constructed with params in provided order
            sql = 'UPDATE Users SET'
            for col in kwargs.keys():
                if col in self.allowed_kwargs:
                    sql = sql + ''.join(f' {col} = (?) ')
                else:
                    raise KeyError(f'Invalid keyword {col}')
            sql = sql + 'WHERE username = (?)'

            params = [value for value in kwargs.values()]
            params.append(username)
            cur.execute(sql, params)
            conn.commit()

    def delete(self, username: str):
        """Delete a User

        :param username: The username of the user to delete
        """
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM Users
                WHERE username = (?)
            """, (username,))
            conn.commit()

    def getUserWithPassword(self, username: str) -> dict:
        """Retrieve the User data with the specified username, including the password

        :param username: The username of the user to be retrieved
        :return: A dictionary containing the user data if found, otherwise None
        """
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            res = cur.execute("""
                SELECT *
                FROM Users
                WHERE username = (?)
            """, (username,))
            row = res.fetchone()
            return row if row else None