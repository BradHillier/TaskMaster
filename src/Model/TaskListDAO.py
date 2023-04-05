import sqlite3
from TaskListSerializer import TaskListSerializer


class TaskListDAO:
    """A data access object for retrieving tasklist data"""

    def __init__(self, db: str):
        self.db = db
        self.serializer = TaskListSerializer()

    def create(self, username: str, list_name: str) -> object:
        """Create a new TaskList

        Params:
            user (str): the username of the creator of the task list
            name (str): the name of the TaskList
        Returns:
            A new TaskList object created by the serializer
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO TaskLists(username, listName)
                VALUES (?, ?)
            """, [username, list_name])
            ID = cur.lastrowid
            conn.commit()
            return self.serializer.serialize( (ID, list_name, username) )

    def getAll(self, username: str ) -> list:
        """Retrieve all the TaskLists owned by a specific user

        Params:
            username (User): The user to get task lists for
        Returns:
            A list containing all TaskList objects owned by the provided user
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            res = cur.execute("""
                SELECT listName, listID
                FROM TaskLists
                WHERE username = (?)
            """, [username])

            all_task_lists = []
            for (name, ID) in res.fetchall():
                task_list = self.serializer.serialize( (ID, name, username) ) 
                all_task_lists.append(task_list)
            return all_task_lists

    def rename(self, task_list_id: int, name: str):
        """Rename a TaskList

        Params:
            task_list (TaskList): The task list to rename
            name (str): the new name for the tasklist
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

        Params:
            task_list (TaskList): The task list to delete
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM TaskLists
                WHERE listID = (?)
            """, [task_list.ID])
            conn.commit()
