from datetime import date
from . import task


class TaskManager:
    '''
    Třída pro vytváření, změnu a vymazání úkolů.

    Attributes:

    tasks : list
        seznam všech vytvořených pkolů
    '''

    def __init__(self):
        self.tasks = []

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
        task_ = kwargs.get("task", None)

        if dl_day and dl_month and dl_year:
            deadline = date(dl_year, dl_month, dl_day)
        else:
            deadline = None
        new_task = task.Task(deadline, task_)
        self.tasks.append(new_task)

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
            tasks_dict[self.tasks.index(task)] = task.__repr__()
        return tasks_dict

    def edit_task(self, manager_index: int, **kwargs):
        '''
        Změní již vytvořený úkol.

        Parameters:
            manager_index : int
                index úkolu v seznamu úkolů manageru (self.tasks)

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
            new_deadline = date(new_dl_year, new_dl_month, new_dl_day)
            self.tasks[manager_index].deadline = new_deadline
        elif deadline == False:
            self.tasks[manager_index].deadline = None

        self.tasks[manager_index].task = new_task

    def delete_task(self, manager_index):
        '''
        Smaže již vytvořený úkol.

        Parametr:
            manager_index : int
                index úkolu v seznamu úkolů manageru (self.tasks)
        '''

        self.tasks.remove(self.tasks[manager_index])
