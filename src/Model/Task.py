from dataclasses import dataclass
from datetime import date

@dataclass
class Task:
    ID: int
    listID: int
    user: str # change to User obj
    name: str
    description: str
    dueDate: date
    isCompleted: bool
    priority: str
