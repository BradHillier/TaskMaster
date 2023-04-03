from Task import Task
import dateparser


class TaskSerializer:

    def deserialize(self, task_data: tuple) -> Task:
        return Task(
            ID = task_data[0],
            listID = task_data[1],
            user = task_data[2],
            name = task_data[3],
            description = task_data[4],
            dueDate = dateparser.parse(task_data[5]),
            isCompleted = task_data[6],
            priority = task_data[7])
