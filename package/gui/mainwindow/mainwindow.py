import tkinter as tk
from ..add_edit.addtaskwindow import AddTaskWindow
from .tasklistframe import TaskListFrame


class MainWindow(tk.Tk):

    def __init__(self, manager):
        super().__init__()
        self.title("Task Manager")
        self.geometry("500x700")
        self.manager = manager

        self.main_menu = tk.Menu(self)

        self.add = tk.Menu(self.main_menu)
        self.add.add_command(label="Add Task", command=self.add_task)
        self.main_menu.add_cascade(label="New", menu=self.add)
        self.config(menu=self.main_menu)

        self.task_list = TaskListFrame(self, self.manager)
        self.task_list.pack(expand=True, fill="both")

    def add_task(self):
        AddTaskWindow(self.manager)
