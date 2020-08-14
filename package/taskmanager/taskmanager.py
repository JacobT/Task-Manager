from datetime import date
from .task import Task


class TaskManager:

    def __init__(self):
        self.tasks = []

    def new_task(self, dl_day: int = None, dl_month: int = None, dl_year: int = None, task: str = 'None'):
        if dl_day and dl_month and dl_year:
            deadline = date(dl_year, dl_month, dl_day)
        else:
            deadline = None
        new_task = Task(deadline, task)
        self.tasks.append(new_task)

    def print(self):
        for task in self.tasks:
            yield task.__repr__()

    def edit_task(self, index: int, **kwargs):
        new_dl_day = kwargs.get("day", None)
        new_dl_month = kwargs.get("month", None)
        new_dl_year = kwargs.get("year", None)
        deadline = kwargs.get("deadline", None)
        new_task = kwargs.get("task", None)

        if new_dl_day and new_dl_month and new_dl_year:
            new_deadline = date(new_dl_year, new_dl_month, new_dl_day)
            self.tasks[index].deadline = new_deadline
        elif deadline == False:
            self.tasks[index].deadline = None

        if new_task:
            self.tasks[index].task = new_task

    def delete_task(self, index):
        self.tasks.remove(self.tasks[index])
