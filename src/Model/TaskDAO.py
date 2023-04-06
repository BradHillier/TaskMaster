import sqlite3
from TaskSerializer import TaskSerializer


def dict_factory(cursor, row):
    """returns each row as a dict, with column names mapped to values

    taken from
    https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory
    """
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


class TaskDAO:

    def __init__(self, db_path: str):
        """Create an instance of the TaskDAO

        :param db_path: The path to the database containing a Task table
        """
        self.db = db_path
        self.serializer = TaskSerializer()

    def create(self, **kwargs) -> int:
        """Create a new Task

        :param listID: The ID of the TaskList the Task will be added to
        :param username: The username of the creator of the Task
        :param taskName: The name of the Task
        :param description: A description of the Task
        :param dueDate: The date the Task is due on, should be a date object
        :param isCompleted: A boolean denoting whether the task has been completed
        :param priority: A string representing the urgency of the Task
        :return: The ID of the newly created Task if successful, otherwise None

        Example
        -------
        ```python3
        from datetime import date


        myTaskDAO = TaskDAO('path/to/database.sqlite3')
        task_data = {
            'listID': 1,
            'username': 'user1',
            'taskName': 'my important task',
            'description': None,
            'dueDate': date.today(),
            'isCompleted': False,
            'priority': 'high'
        }
        new_task_id = myTaskDAO.create(**task_data)
        ```
        """
        task_data = self.serializer.serialize(req_all=True, **kwargs) 
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = 1") # enables FK constraints
            cur.execute("""
                INSERT INTO Tasks (
                    listID, 
                    username, 
                    taskName, 
                    description,
                    dueDate, 
                    isCompleted, 
                    priority)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, task_data)
            conn.commit()
            return cur.lastrowid

    def getTask(self, task_id: int) -> object:
        """Retreive the Task with the specified ID

        :param task_id: The ID of the task to be retreived
        :return: An object created by serializing the retreived data

        Example
        -------
        ```python3
        my_task_dao = TaskDAO('path/to/database.sqlite3')
        task_id = 1
        my_task_obj = my_task_dao.getTask(task_id)
        ```
        """
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            res = cur.execute("""
                SELECT *
                FROM Tasks
                WHERE taskID = (?)
            """, [task_id])
            return self.serializer.deserialize(**res.fetchone())

    def getTasks(self, list_id: int) -> list:
        """Get all the tasks contained in a specific list

        The type of objects contained within the list are determined by
        the serializer.

        :param list_id: The ID of the task list for which to retreive tasks
        :return: A list containing all Tasks within the specified list

        Example
        -------
        ```python3
        my_task_dao = TaskDAO('path/to/database.sqlite3')
        task_list_id = 1
        my_list_of_task_objs = my_task_dao.getTasks(task_id)
        ```
        """
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            res = cur.execute("""
                SELECT *
                FROM Tasks
                WHERE listID = (?)
            """, [list_id])
            return  [self.serializer.deserialize(**row) for (row) in res.fetchall()]

    def update(self, task_id: int, **kwargs):
        """
        :param task_id:

        Example
        -------
        ```python3
        from datetime import date, timedelta


        my_task_dao = TaskDAO('path/to/database.sqlite3')
        my_task_id = 1
        task_data = {
            'description': 'detailed description of task',
            'dueDate': date.today() + timedelta(days=3),
        }
        my_task_dao.update(my_task_id, **task_data)
        ```

        \u26A0 WARNING
        -------
        The SQL statement executed by this function is dynamically created. 
        All input from the user has been sanitized, but column names provided 
        by the developer are directly inserted into the string. They are first 
        checked against a list of allowed keywords, but this still opens a 
        potential security risk.
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()

            # stmt is constructed with params in provided order            
            sql = 'UPDATE Tasks SET'
            for col in kwargs.keys(): 
                if col in self.allowed_kwargs:
                    sql = sql + ''.join(f' {col} = (?) ')
                else:
                    raise KeyError(f'Invalid keyword {col}')
            sql = sql + 'WHERE taskID = (?)'

            params = [value for value in kwargs.values()]
            params.append(task_id)
            cur.execute(sql, params) 
            conn.commit()

    def delete(self, task_id: int):
        """Delete a Task

        :param task_id: The ID of the task to delete
        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM Tasks
                WHERE taskID = (?)
            """, [task_id])
            conn.commit()
