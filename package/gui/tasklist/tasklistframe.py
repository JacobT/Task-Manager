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
        task_frame = tk.Frame(self)
        task_label = tk.Label(task_frame, text=task)
        task_label.pack()
        return task_frame
