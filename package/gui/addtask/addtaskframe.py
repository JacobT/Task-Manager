import tkinter as tk
from .taskframe import TaskFrame
from .deadlineframe import DeadlineFrame


class AddTaskFrame(tk.LabelFrame):

    def __init__(self, root, manager):
        super().__init__(root, padx=10)
        self.manager = manager

        self.deadline_frame = DeadlineFrame(self)
        self.deadline_frame.grid(row=1, column=1, sticky="nswe")

        self.task_frame = TaskFrame(self)
        self.task_frame.grid(row=1, column=2, padx=10, pady=5, rowspan=2, sticky="nswe")

        self.add_task_button = tk.Button(self, text='Add Task',
                                         command=self.click)
        self.add_task_button.grid(row=1, column=3, pady=5, sticky="n")

        self.print_frame = tk.Frame(self)
        self.print_frame.grid(row=3, column=1, columnspan=3)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.pack(padx=5, pady=5, expand=True, fill="both")

    def click(self):
        for slave in self.print_frame.pack_slaves():
            slave.destroy()

        day = self.deadline_frame.day_var.get()
        month = self.deadline_frame.month_var.get()
        year = self.deadline_frame.year_var.get()
        task = self.task_frame.task.get(1.0, 'end').strip()
        try:
            if day != None and self.deadline_frame.deadline_var.get():
                self.manager.new_task(day, month, year, task)
            else:
                self.manager.new_task(task=task)
        except Exception as e:
            e_label = tk.Label(self.print_frame, text=str(e))
            e_label.pack()
        finally:
            # self.destroy()
            pass

        label = tk.Label(self.print_frame, text=str(self.manager.tasks[-1]))
        label.pack()
