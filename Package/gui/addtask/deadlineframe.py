import tkinter as tk
from tkinter import Frame


class DeadlineFrame(tk.Frame):

    def __init__(self, parent, day_var, month_var, year_var, deadline_var):
        super().__init__(parent)

        self.day_var = day_var
        self.month_var = month_var
        self.year_var = year_var
        self.deadline_var = deadline_var

        deadline = tk.Checkbutton(self, text='Deadline',
                                  variable=self.deadline_var, command=self._dl_check)
        deadline.pack()

        self.date_frame = Frame(self)

        days = [i for i in range(1, 32)]
        day = tk.OptionMenu(self.date_frame, self.day_var, *days)
        day.grid(row=1, column=1)

        months = [i for i in range(1, 13)]
        month = tk.OptionMenu(self.date_frame, self.month_var, *months)
        month.grid(row=1, column=2)

        years = [i for i in range(2020, 2050)]
        year = tk.OptionMenu(self.date_frame, self.year_var, *years)
        year.grid(row=1, column=3)

        self.date_frame.pack(expand=True)

    def _dl_check(self):
        if self.deadline_var.get():
            for slave in self.date_frame.grid_slaves():
                slave.configure(state=tk.NORMAL)
        else:
            for slave in self.date_frame.grid_slaves():
                slave.configure(state=tk.DISABLED)
