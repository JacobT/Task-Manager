import tkinter as tk


class TaskFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bd=2, relief=tk.SUNKEN)

        self.task = tk.Text(self, width=30, height=4)
        self.task.pack(side=tk.LEFT, fill=tk.Y)

        self.task_scroll = tk.Scrollbar(self)
        self.task.config(yscrollcommand=self.task_scroll.set)
        self.task_scroll.config(command=self.task.yview)
        self.task_scroll.pack()
