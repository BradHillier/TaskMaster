from TaskList import TaskList

class TaskListSerializer:

    def serialize(self, data: tuple):
        return TaskList(ID=data[0], name=data[1], user=data[2])

    def deserialize(task_list: TaskList):
        pass

