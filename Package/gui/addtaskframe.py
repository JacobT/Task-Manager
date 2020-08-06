import tkinter as tk
from .taskframe import TaskFrame


class AddTaskFrame(tk.LabelFrame):

    def __init__(self, root, manager):
        super().__init__(root, padx=10)
        self.manager = manager

        self.day_var = tk.StringVar(value='Day')
        self.month_var = tk.StringVar(value='Month')
        self.year_var = tk.StringVar(value='Year')
        self.deadline_var = tk.BooleanVar(value=True)
        self.deadline_frame = self.deadline_frame()
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
        try:
            if day.isdigit() and month.isdigit() and year.isdigit() and self.deadline_var.get():
                self.manager.new_task(int(day), int(month), int(year),
                                      self.task_frame.task.get(1.0, 'end').strip())
            else:
                self.manager.new_task(
                    task=self.task_frame.task.get(1.0, 'end').strip())
        except Exception as e:
            e_label = tk.Label(self.print_frame, text=str(e))
            e_label.pack()
        finally:
            # self.destroy()
            pass

        self.task_frame.task.delete(1.0, 'end')
        self.day_var.set("Day")
        self.month_var.set("Month")
        self.year_var.set("Year")

        label = tk.Label(self.print_frame, text=str(self.manager.tasks[-1]))
        label.pack()

    def deadline_frame(self):
        deadline_frame = tk.Frame(self, width=60)

        days = [i for i in range(1, self._dl_date())]
        day = tk.OptionMenu(deadline_frame, self.day_var, *days)
        day.grid(row=1, column=1)

        months = [i for i in range(1, 13)]
        month = tk.OptionMenu(deadline_frame, self.month_var, *months)
        month.grid(row=1, column=2)

        years = [i for i in range(2020, 2050)]
        year = tk.OptionMenu(deadline_frame, self.year_var, *years)
        year.grid(row=1, column=3)

        deadline = tk.Checkbutton(deadline_frame, text='Deadline',
                                  variable=self.deadline_var, command=self._dl_check)
        deadline.grid(row=0, column=1, columnspan=3, sticky="s")

        return deadline_frame

    def _dl_date(self):
        if self.month_var.get() in [1, 3, 5, 7, 8, 10, 12]:
            return 32
        else:
            return 31

    def _dl_check(self):
        if self.deadline_var.get():
            for slave in self.deadline_frame.grid_slaves():
                slave.configure(state=tk.NORMAL)
        else:
            for slave in self.deadline_frame.grid_slaves():
                slave.configure(state=tk.DISABLED)
