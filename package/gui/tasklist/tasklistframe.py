import tkinter as tk


class TaskListFrame(tk.LabelFrame):

    def __init__(self, root, manager):
        super().__init__(root)

        self.manager = manager

        self.tasks = []

        if len(self.manager.tasks) >= 1:
            for task in self.manager.print():
                task_frame = self.task_frame(task)
                self.tasks.append(task)
                task_frame.pack()
        else:
            label = tk.Label(self, text="No tasks yet.")
            label.pack()

        self.pack(padx=5, pady=5, expand=True, fill="both")

    def task_frame(self, task):
        task_created, task_modified, task_deadline, task_task = task

        task_frame = tk.Frame(self)

        created_label = tk.Label(task_frame, text=task_created)
        created_label.grid(row=1, column=1)

        modified_label = tk.Label(task_frame, text=task_modified)
        modified_label.grid(row=1, column=2)

        deadline_label = tk.Label(task_frame, text=task_deadline)
        deadline_label.grid(row=1, column=3)

        task_label = tk.Label(task_frame, text=task_task)
        task_label.grid(row=1, column=4)

        return task_frame
