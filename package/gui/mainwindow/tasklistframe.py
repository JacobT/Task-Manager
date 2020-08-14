import tkinter as tk


class TaskListFrame(tk.LabelFrame):

    def __init__(self, root, manager):
        super().__init__(root)
        self.pack(padx=5, pady=5, expand=True, fill="both")

        self.manager = manager

        self.tasks = []
        self.update_list()

        self.bind_all("<<update_list>>", self.update_list)

    def update_list(self, *args):
        for task in self.tasks:
            task.destroy()

        if len(self.manager.tasks) >= 1:
            for task in self.manager.print():
                task_frame = self._task_frame(task)
                task_frame.pack()
                self.tasks.append(task_frame)
        else:
            label = tk.Label(self, text="No tasks yet.")
            label.pack()
            self.tasks.append(label)

    def _task_frame(self, task):
        task_created, task_modified, task_deadline, task_task = task

        task_frame = tk.Frame(self)

        created_label = tk.Label(task_frame, text=task_created)
        created_label.grid(row=1, column=1)

        modified_label = tk.Label(task_frame, text=task_modified)
        modified_label.grid(row=1, column=3)

        deadline_label = tk.Label(task_frame, text=task_deadline)
        deadline_label.grid(row=1, column=5)

        task_label = tk.Label(task_frame, text=task_task)
        task_label.grid(row=1, column=7)

        task_frame.grid_columnconfigure(0, weight=1)
        task_frame.grid_columnconfigure(1, minsize=125)
        task_frame.grid_columnconfigure(3, minsize=125)
        task_frame.grid_columnconfigure(5, minsize=125)
        task_frame.grid_columnconfigure(7, minsize=125)
        task_frame.grid_columnconfigure(8, weight=1)

        return task_frame