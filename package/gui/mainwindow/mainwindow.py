import tkinter as tk
from ..add_edit import addtaskwindow
from . import taskdisplayframe


class MainWindow(tk.Tk):
    '''Hlavní okno aplikace.'''

    def __init__(self, manager):
        super().__init__()
        self.title("Task Manager")
        self.geometry("700x500")

        self.manager = manager
        self.tasks = []

        # nabídka okna
        self.main_menu = tk.Menu(self)
        self.add = tk.Menu(self.main_menu)
        self.add.add_command(label="Add Task", command=self.add_task)
        self.main_menu.add_cascade(label="New", menu=self.add)
        self.config(menu=self.main_menu)

        # frame pro zobrazení úkolů
        self.task_list = tk.LabelFrame(self)
        self.task_list.pack(padx=5, pady=5, expand=True, fill="both")

        self._update_task_list()
        self.bind_all("<<update_task_list>>", self._update_task_list)

    def add_task(self):
        '''Funkce tlačítka pro vytvoření nového úkolu.'''

        addtaskwindow.AddTaskWindow(self.manager)

    def _update_task_list(self, *event):
        for task in self.tasks:
            task.destroy()

        manager_tasks = self.manager.get_tasks()
        if manager_tasks:
            for task in manager_tasks:
                task_frame = taskdisplayframe.TaskFrame(self.task_list, self.manager,
                                                        task, **manager_tasks[task])
                task_frame.pack()
                self.tasks.append(task_frame)
        else:
            no_tasks_label = tk.Label(self.task_list, text="No tasks yet.")
            no_tasks_label.pack()
            self.tasks.append(no_tasks_label)
