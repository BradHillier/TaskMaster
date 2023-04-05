import sqlite3
from TaskListSerializer import TaskListSerializer


def dict_factory(cursor, row):
    """returns each row as a dict, with column names mapped to values

    taken from
    https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory
    """
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


class TaskListDAO:
    """A data access object for retrieving tasklist data
    
    The database being accessed should contain a TaskLists table
    with the following columns:

            listID: int
            listName: str
            username: str
    """

    def __init__(self, db_path: str):
        """Create an instance of the TaskListDAO

        :param db_path: The path to the database containing a TaskLists table
        """
        self.db = db_path
        self.serializer = TaskListSerializer()
        """Converts retreived table rows of task list data into objects"""

    def create(self, username: str, list_name: str) -> int:
        """Create a new TaskList

        :param user: the username of the creator of the task list
        :param name: the name of the TaskList
        :return: The ID of the newly created task if successful, othewise None
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO TaskLists(username, listName)
                VALUES (?, ?)
            """, [username, list_name])
            return cur.lastrowid

    def getOne(self, listID: int) -> object:
        """Retrieve the TaskList with the specified ID

        :param listID: The ID of the task list to retreive
        :return: An object created by deserializing the retreived data
        """
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            res = cur.execute("""
                SELECT * 
                FROM TaskLists
                WHERE listID = (?)
            """, [listID])
            return self.serializer.deserialize(**res.fetchone())

    def getAll(self, username: str ) -> list:
        """Retrieve all the TaskLists owned by a specific user

        :param username: The user to get task lists for
        :return: A list containing all TaskList objects owned by the provided user
        """
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            res = cur.execute("""
                SELECT listName, listID
                FROM TaskLists
                WHERE username = (?)
            """, [username])

            return [self.serializer.deserialize(**row) for row in res.fetchall()]

    def rename(self, task_list_id: int, name: str):
        """Rename a TaskList

        :param task_list: The task list to rename
        :param name: the new name for the tasklist
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE TaskLists
                SET listName = (?)
                WHERE listID = (?)
            """, [name, task_list_id])
            conn.commit()

    def delete(self, task_list_id: int):
        """Delete a TaskList

        :param task_list: The task list to delete
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM TaskLists
                WHERE listID = (?)
            """, [task_list_id])
            conn.commit()
