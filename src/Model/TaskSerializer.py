from src.Model.Task import Task
import dateparser


class TaskSerializer:

    allowed_kwargs = [
            'listID',
            'username',
            'taskName',
            'description',
            'dueDate',
            'isCompleted',
            'priority']

    def serialize(self, req_all=False, **kwargs):

        # Check for any unexpected keywords
        unexpected_keys = [key for key in kwargs if key not in self.allowed_kwargs]
        if len(unexpected_keys) != 0:
            raise TypeError(f'Unexpected keyword arguments {unexpected_keys}')

        # If all keywords are required, ensure they were provided
        if req_all == True:
            missing_keys = [key for key in self.allowed_kwargs if key not in kwargs]
            if len(missing_keys) != 0:
                raise KeyError(f'Missing required keywords {missing_keys}')

        if 'dueDate' in kwargs:
            kwargs['dueDate'] = kwargs['dueDate'].isoformat()

        # ensure values appear in the expected order
        return tuple(kwargs[key] for key in self.allowed_kwargs if key in kwargs)


    def deserialize(self, **kwargs) -> Task:
        return Task(
                ID = kwargs.get('taskID'),
                listID = kwargs.get('listID'),
                user = kwargs.get('username'),
                name = kwargs.get('taskName'),
                description = kwargs.get('description'),
                dueDate = kwargs.get('dueDate'),
                isCompleted = kwargs.get('isCompleted'),
                priority = kwargs.get('priority'))


