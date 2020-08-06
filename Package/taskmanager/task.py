import datetime


class Task:

    def __init__(self, deadline: datetime.date = None, task: str = 'None'):
        self.created = datetime.date.today()
        self._modified = datetime.datetime.now()
        self.deadline = deadline
        self.task = task

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, creation_date):
        if not hasattr(self, '_created'):
            self._created = creation_date
        else:
            raise AttributeError('Creation date cannot be changed.')

    @property
    def modified(self):
        return self._modified

    def _modify(self):
        self._modified = datetime.datetime.now()

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, new_deadline: datetime.date):
        if isinstance(new_deadline, datetime.date) and new_deadline >= self.created:
            self._deadline = new_deadline
            self._modify()
        elif not new_deadline:
            self._deadline = None
        else:
            raise AttributeError('Invalid deadline.')

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, new_task: str):
        if isinstance(new_task, str):
            self._task = new_task
            self._modify()
        else:
            raise AttributeError('Invalid task.')

    def __str__(self):
        return f"Date created: {self.created}\nDate modified: {self.modified}\nDeadline: {self.deadline}\nTask: {self.task}"
