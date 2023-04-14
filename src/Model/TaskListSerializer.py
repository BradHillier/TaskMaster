from src.Model.TaskList import TaskList

class TaskListSerializer:

    def serialize(self, **kwargs):
        raise NotImplemented

    def deserialize(self, **kwargs):
        return TaskList(
            ID = kwargs.get('listID'), 
            name = kwargs.get('listName'), 
            user = kwargs.get('username'))

