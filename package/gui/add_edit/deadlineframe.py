import tkinter as tk
import datetime


class DeadlineFrame(tk.Frame):

    def __init__(self, parent, warning_var):
        super().__init__(parent)

        self.warning_var = warning_var

        # vytvoření deadline checkbuttonu
        self.deadline_var = tk.BooleanVar(value=True)
        deadline = tk.Checkbutton(self, text='Deadline',
                                  variable=self.deadline_var,
                                  command=self._dl_check)
        deadline.pack()

        # frame pro optionmenu data
        self.date_frame = tk.Frame(self)
        self.date_frame.pack()

        self.today = datetime.date.today()

        # optionmenu určující den
        self.day_var = tk.IntVar()
        days = [i for i in range(self.today.day, 32)]
        self.day = tk.OptionMenu(self.date_frame, self.day_var, *days)
        self.day.grid(row=1, column=1, sticky="WE")
        self.day_var.trace("w",
                           lambda *args: self.day.config(bg=self.cget("bg")))

        # optionmenu určující měsíc
        self.month_var = tk.IntVar()
        months = [i for i in range(self.today.month, 13)]
        self.month = tk.OptionMenu(self.date_frame, self.month_var, *months)
        self.month.grid(row=1, column=2, sticky="WE")
        self.month_var.trace("w", self._date_check)

        # optionmenu určující rok
        self.year_var = tk.IntVar()
        years = [i for i in range(self.today.year, self.today.year + 10)]
        self.year = tk.OptionMenu(self.date_frame, self.year_var, *years)
        self.year.grid(row=1, column=3, sticky="WE")
        self.year_var.trace("w", self._date_check)

        # výchozí hodnoty (aktuální datum)
        self.day_var.set(self.today.day)
        self.month_var.set(self.today.month)
        self.year_var.set(self.today.year)

        self.date_frame.grid_columnconfigure(1, minsize=60)
        self.date_frame.grid_columnconfigure(2, minsize=60)
        self.date_frame.grid_columnconfigure(3, minsize=70)

    def _dl_check(self):
        if self.deadline_var.get():
            for slave in self.date_frame.grid_slaves():
                slave.configure(state=tk.NORMAL)
        else:
            for slave in self.date_frame.grid_slaves():
                slave.configure(state=tk.DISABLED)

    @staticmethod
    def _change_options(optionmenu, new_options, optionmenu_var):
        optionmenu["menu"].delete(0, "end")
        for option in new_options:
            optionmenu["menu"].add_command(label=option,
                                           command=tk._setit(optionmenu_var, option))

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

        if selected_month == self.today.month and selected_year == self.today.year:
            days_min = self.today.day
        else:
            days_min = 1

        new_days = [i for i in range(days_min, days_max + 1)]

        if self.day_var.get() not in new_days:
            self.day.config(bg="red")
        else:
            self.day.config(bg=self.cget("bg"))

        self._change_options(self.day, new_days, self.day_var)

        if selected_year == self.today.year:
            if selected_month < self.today.month:
                self.month.config(bg="red")
            else:
                self.month.config(bg=self.cget("bg"))
            new_months = [i for i in range(self.today.month, 13)]
            self._change_options(self.month, new_months, self.month_var)
        else:
            self.month.config(bg=self.cget("bg"))
            new_months = [i for i in range(1, 13)]
            self._change_options(self.month, new_months, self.month_var)
