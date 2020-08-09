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
            print(f'{self.tasks.index(task) + 1}.\n{task}')

    def edit_task(self, index, new_deadline=None, new_task: str = 'None'):
        if new_deadline:
            self.tasks[index].deadline = new_deadline
        if new_task:
            self.tasks[index].task = new_task

    def delete_task(self, index):
        self.tasks.remove(self.tasks[index])
