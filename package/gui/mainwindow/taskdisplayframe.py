import tkinter as tk


class TaskFrame(tk.Frame):
    '''Frame pro zobrazení úkolu.'''

    def __init__(self, parent, index, created, modified, deadline, task):
        super().__init__(parent)

        self.created = tk.StringVar()
        self.modified = tk.StringVar()
        self.deadline = tk.StringVar()
        self.task = tk.StringVar()

        self.created.set(created)
        self.modified.set(modified)
        self.deadline.set(deadline)
        self.task.set(task)
        self.manager_index = index

        self._task_frame()

    def _task_frame(self):
        # štítky pro zobrazení úkolu
        created_label = tk.Label(self, textvariable=self.created)
        created_label.grid(row=1, column=1)

        modified_label = tk.Label(self, textvariable=self.modified)
        modified_label.grid(row=1, column=3)

        deadline_label = tk.Label(self, textvariable=self.deadline)
        deadline_label.grid(row=1, column=5)

        task_label = tk.Label(self, textvariable=self.task)
        task_label.grid(row=1, column=7)

        # tlačítko pro editaci
        destroy_button = tk.Button(self, text="Edit", command=self._edit_task)
        destroy_button.grid(row=1, column=8)

        # tlačítko pro smazání
        destroy_button = tk.Button(self, text="X", command=self._destroy_task)
        destroy_button.grid(row=1, column=9)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, minsize=125)
        self.grid_columnconfigure(3, minsize=125)
        self.grid_columnconfigure(5, minsize=125)
        self.grid_columnconfigure(7, minsize=125)
        self.grid_columnconfigure(8, minsize=50)
        self.grid_columnconfigure(9, minsize=50)
        self.grid_columnconfigure(10, weight=1)

    def _edit_task(self):
        pass

    def _destroy_task(self):
        pass
