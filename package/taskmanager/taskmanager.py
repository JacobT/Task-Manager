import datetime
from . import task
import sqlite3


class TaskManager:
    '''
    Třída pro vytváření, změnu a vymazání úkolů.

    Attributes:

    tasks : list
        seznam všech vytvořených pkolů
    '''

    def __init__(self):
        self.tasks = {}
        self.connect = sqlite3.connect("database/taskmanager.db",
                                       detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self._load_db()

    def __del__(self):
        self.connect.close()

    def new_task(self, **kwargs):
        '''
        Vytvoření nového úkolu.

        Keyword arguments:
            day : int | None = None
                datum deadline - den

            month : int | None = None
                datum deadline - měsíc

            year : int | None = None
                datum deadline - rok

            task : str | None = None
                popis úkolu
        '''

        dl_day = kwargs.get("day", None)
        dl_month = kwargs.get("month", None)
        dl_year = kwargs.get("year", None)
        task_desc = kwargs.get("task", None)

        if dl_day and dl_month and dl_year:
            deadline = datetime.date(dl_year, dl_month, dl_day)
        else:
            deadline = None

        new_task = task.Task(deadline, task_desc)

        # zápis do databáze
        cursor = self.connect.cursor()
        cursor.execute("INSERT INTO tasks VALUES (?,?,?,?)", new_task.to_db())
        self.connect.commit()

        new_task.id = cursor.lastrowid
        self.tasks[new_task.id] = new_task

    def get_tasks(self):
        '''
        Navrací slovník všech úkolů ve tvaru {index : task}

            index : index úkolu v manageru (self.tasks)

            task : slovník s reprezentací úkolu
                "created" : str
                    datum vytvoření

                "modified" : str
                    datum poslední změny

                "deadline" : str
                    datum deadline

                "task" : str
                    popis úkolu
        '''

        tasks_dict = {}
        for task in self.tasks:
            tasks_dict[task] = self.tasks[task].get_dict()
        return tasks_dict

    def edit_task(self, id: int, **kwargs):
        '''
        Změní již vytvořený úkol.

        Parameters:
            id : int
                id úkolu v databázi (self.tasks)

        Keyword arguments:
            day : int | None = None
                datum deadline - den

            month : int | None = None
                datum deadline - měsíc

            year : int | None = None
                datum deadline - rok

            task : str | None = None
                popis úkolu

            deadline : bool | None = None
                True, None - nic nemění
                False - změní deadline úkolu na None
        '''

        new_dl_day = kwargs.get("day", None)
        new_dl_month = kwargs.get("month", None)
        new_dl_year = kwargs.get("year", None)
        deadline = kwargs.get("deadline", None)
        new_task = kwargs.get("task", None)

        if new_dl_day and new_dl_month and new_dl_year:
            new_deadline = datetime.date(new_dl_year, new_dl_month, new_dl_day)
            self.tasks[id].deadline = new_deadline
        elif deadline == False:
            self.tasks[id].deadline = None

        self.tasks[id].task = new_task

        # zápis do databáze
        cursor = self.connect.cursor()
        cursor.execute("""
            UPDATE tasks
            SET created=?,
                modified=?,
                deadline=?,
                task=?
            WHERE rowid=?
            """, self.tasks[id].to_db())
        self.connect.commit()

    def delete_task(self, id):
        '''
        Smaže již vytvořený úkol.

        Parametr:
            id : int
                id úkolu v databázi (self.tasks)
        '''

        self.tasks.pop(id)

        # vymazání z databáze
        cursor = self.connect.cursor()
        cursor.execute("DELETE FROM tasks WHERE rowid=?", (id,))
        self.connect.commit()

    def _load_db(self):
        cursor = self.connect.cursor()
        cursor.execute("SELECT rowid, * FROM tasks")
        for row in cursor.fetchall():
            id, creation, modified, deadline, task_desc = row
            new_task = task.Task(deadline, task_desc, creation, modified, id)
            self.tasks[new_task.id] = new_task
