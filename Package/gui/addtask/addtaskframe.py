import tkinter as tk
from .taskframe import TaskFrame
from .deadlineframe import DeadlineFrame


class AddTaskFrame(tk.LabelFrame):

    def __init__(self, root, manager):
        super().__init__(root, padx=10)
        self.manager = manager

        self.day_var = tk.IntVar()
        self.month_var = tk.IntVar()
        self.year_var = tk.IntVar()
        self.deadline_var = tk.BooleanVar(value=True)
        self.deadline_frame = DeadlineFrame(self, self.day_var, self.month_var,
                                            self.year_var, self.deadline_var)
        self.deadline_frame.grid(row=2, column=1, sticky="nswe")

        self.task_frame = TaskFrame(self)
        self.task_frame.grid(row=1, column=2, padx=10, pady=5, rowspan=2)

        self.add_task_button = tk.Button(self, text='Add Task',
                                         command=self.click)
        self.add_task_button.grid(row=1, column=3, rowspan=2)

        self.print_frame = tk.Frame(self)
        self.print_frame.grid(row=3, column=1, columnspan=3)

        self.pack(padx=5, pady=5, expand=True, fill="both")

    def click(self):
        for slave in self.print_frame.pack_slaves():
            slave.destroy()

        day = self.day_var.get()
        month = self.month_var.get()
        year = self.year_var.get()
        task = self.task_frame.task.get(1.0, 'end').strip()
        try:
            if day != None and self.deadline_var.get():
                self.manager.new_task(day, month, year, task)
            else:
                self.manager.new_task(task=task)
        except Exception as e:
            e_label = tk.Label(self.print_frame, text=str(e))
            e_label.pack()
        finally:
            # self.destroy()
            pass

        # self.task_frame.task.delete(1.0, 'end')
        # self.day_var.set("Day")
        # self.month_var.set("Month")
        # self.year_var.set("Year")

        label = tk.Label(self.print_frame, text=str(self.manager.tasks[-1]))
        label.pack()
