import tkinter as tk


class TaskListFrame(tk.LabelFrame):

    def __init__(self, root, manager):
        super().__init__(root)

        self.manager = manager

        self.tasks = []

        if len(self.manager.tasks) >= 1:
            for task in self.manager.tasks:
                task_frame = tk.Frame(self)
                self.tasks.append(task)
                task_frame.pack()
        else:
            label = tk.Label(self, text="No tasks yet.")
            label.pack()

        self.pack(padx=5, pady=5, expand=True, fill="both")
