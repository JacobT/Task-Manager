import tkinter as tk
from . import taskframe
from . import deadlineframe


class AddTaskWindow(tk.Toplevel):
    '''Okno pro vytvoření nového úkolu.'''

    def __init__(self, manager):
        super().__init__()
        self.manager = manager

        self.title("Add Task")

        self.main_frame = tk.LabelFrame(self, padx=10)
        self.main_frame.pack(padx=5, pady=5, expand=True, fill="both")

        # vytvoření tlačítek
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.grid(row=1, column=3, pady=5, sticky="nswe")

        self.confirm_button = tk.Button(self.button_frame,
                                        text="OK",
                                        width=10,
                                        command=self.confirm_click)
        self.confirm_button.pack()

        self.cancel_button = tk.Button(self.button_frame,
                                       text="Cancel",
                                       width=10,
                                       command=self.destroy)
        self.cancel_button.pack(pady=5)

        # štítek pro zobrazení varování
        self.warning_var = tk.StringVar("")
        self.warning_label = tk.Label(self.main_frame,
                                      textvariable=self.warning_var)
        self.warning_label.grid(row=3, column=1, columnspan=3)

        # checkbutton a optionmenu pro určení deadline
        self.deadline_frame = deadlineframe.DeadlineFrame(self.main_frame,
                                                          self.warning_var)
        self.deadline_frame.grid(row=1, column=1, pady=5, sticky="nswe")

        # textové pole úkolu
        self.task_frame = taskframe.TaskFrame(self.main_frame)
        self.task_frame.grid(row=1, column=2, rowspan=2,
                             padx=10, pady=5,
                             sticky="nswe")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

    def confirm_click(self):
        '''Funkce potvrzovacího tlačítka.'''

        self.warning_var.set("")

        day = self.deadline_frame.day_var.get()
        month = self.deadline_frame.month_var.get()
        year = self.deadline_frame.year_var.get()
        task = self.task_frame.task.get(1.0, "end").strip()
        try:
            self._confirm_func(day, month, year, task)
            self.event_generate("<<update_task_list>>")
            self.destroy()
        except Exception as e:
            self.warning_var.set(e)

    def _confirm_func(self, day, month, year, task):
        if self.deadline_frame.deadline_var.get():
            self.manager.new_task(day=day, month=month, year=year, task=task)
        else:
            self.manager.new_task(task=task)
