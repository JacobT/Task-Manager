import tkinter as tk
import datetime


class DeadlineFrame(tk.Frame):

    def __init__(self, parent, day_var, month_var, year_var, deadline_var):
        super().__init__(parent)

        self.day_var = day_var
        self.day_var.trace("w", lambda *args: self.day.config(bg="white"))
        self.month_var = month_var
        self.month_var.trace("w", self._date_check)
        self.year_var = year_var
        self.year_var.trace("w", self._date_check)
        self.deadline_var = deadline_var

        deadline = tk.Checkbutton(self, text='Deadline',
                                  variable=self.deadline_var, command=self._dl_check)
        deadline.pack()

        self.date_frame = tk.Frame(self)

        today = datetime.date.today()

        self.day_var.set(today.day)
        days = [i for i in range(1, 32)]
        self.day = tk.OptionMenu(self.date_frame, self.day_var, *days)
        self.day.grid(row=1, column=1)

        self.month_var.set(today.month)
        months = [i for i in range(1, 13)]
        self.month = tk.OptionMenu(self.date_frame, self.month_var, *months)
        self.month.grid(row=1, column=2)

        self.year_var.set(today.year)
        years = [i for i in range(today.year, today.year + 10)]
        self.year = tk.OptionMenu(self.date_frame, self.year_var, *years)
        self.year.grid(row=1, column=3)

        self.date_frame.pack(expand=True)

    def _dl_check(self):
        if self.deadline_var.get():
            for slave in self.date_frame.grid_slaves():
                slave.configure(state=tk.NORMAL)
        else:
            for slave in self.date_frame.grid_slaves():
                slave.configure(state=tk.DISABLED)

    def _date_check(self, *args):
        is_leap_year = False
        selected_year = self.year_var.get()
        if selected_year % 4 == 0 and (selected_year % 100 != 0 or selected_year % 400 == 0):
            is_leap_year = True

        selected_month = self.month_var.get()
        if selected_month == 2 and is_leap_year:
            days_max = 29
        elif selected_month == 2:
            days_max = 28
        elif selected_month in [1, 3, 5, 7, 8, 10, 12]:
            days_max = 31
        else:
            days_max = 30

        new_days = [i for i in range(1, days_max + 1)]

        if self.day_var.get() not in new_days:
            self.day.config(bg="red")

        self.day["menu"].delete(0, "end")
        for day in new_days:
            self.day["menu"].add_command(label=day,
                                         command=tk._setit(self.day_var, day))
