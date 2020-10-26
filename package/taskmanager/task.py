import datetime


class Task:
    '''
    Třída úkolu pro Task Manager.

    Attributes:

        created : date | None (Read-only) -> str
            datum vytvoření úkolu

        deadline : date | None  -> str | None
            datum deadline

        task : str | None -> str
            popis úkolu

        modified : datetime (Read-only) -> str
            datum a čas poslední změny
    '''

    def __init__(self, deadline: datetime.date = None, task: str = "None", creation_date: datetime.date = None, modified: datetime.datetime = None, id: int = None):
        if id and isinstance(id, int):
            self.id = id

        if creation_date and isinstance(creation_date, datetime.date):
            self.created = creation_date
        else:
            self.created = datetime.date.today()

        self.deadline = deadline
        self.task = task

        if modified and isinstance(modified, datetime.datetime):
            self._modified = modified

    @property
    def id(self):
        if hasattr(self, "_id"):
            return self._id

    @id.setter
    def id(self, id: int):
        if not hasattr(self, "_id") or self._id == None:
            self._id = id
        else:
            raise AttributeError("ID cannot be changed.")

    @property
    def created(self):
        return self._created.strftime("%d.%m.%Y")

    @created.setter
    def created(self, creation_date: datetime.date):
        if not hasattr(self, "_created"):
            self._created = creation_date
        else:
            raise AttributeError("Creation date cannot be changed.")

    @property
    def modified(self):
        return self._modified.strftime("%d.%m.%Y %H:%M")

    def _modify(self):
        self._modified = datetime.datetime.now()

    @property
    def deadline(self):
        if self._deadline:
            return self._deadline.strftime("%d.%m.%Y")

    @deadline.setter
    def deadline(self, new_deadline: datetime.date):
        if isinstance(new_deadline, datetime.date) and new_deadline >= datetime.date.today():
            self._deadline = new_deadline
            self._modify()
        elif not new_deadline:
            self._deadline = None
        else:
            raise AttributeError("Invalid deadline.")

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, new_task: str):
        if not new_task:
            new_task = "None"
        if isinstance(new_task, str):
            self._task = new_task
            self._modify()
        else:
            raise AttributeError("Invalid task.")

    def get_dict(self) -> dict:
        '''
        Navrací slovník úkolu:
            "created" : str
                datum vytvoření

            "modified" : str
                datum poslední změny

            "deadline" : str | None
                datum deadline

            "task" : str
                popis úkolu
        '''

        return {"created": self.created,
                "modified": self.modified,
                "deadline": self.deadline,
                "task": self.task}

    def to_db(self):
        if self.id:
            return [self._created, self._modified, self._deadline, self.task, self.id]
        else:
            return [self._created, self._modified, self._deadline, self.task]

    def __str__(self) -> str:
        return f"Date created: {self.created}\nDate modified: {self.modified}\nDeadline: {self.deadline}\nTask: {self.task}"
