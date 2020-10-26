from . import addtaskwindow


class EditTaskWindow(addtaskwindow.AddTaskWindow):

    def __init__(self, manager, id, deadline, task):
        super().__init__(manager)

        self.title("Edit Task")

        self.id = id

        if deadline != "None":
            dl_day, dl_month, dl_year = deadline.split(".")
            self.deadline_frame.year_var.set(int(dl_year))
            self.deadline_frame.month_var.set(int(dl_month))
            self.deadline_frame.day_var.set(int(dl_day))
            self.deadline_frame.deadline_var.set(True)

        if task != "None":
            self.task_frame.task.insert("end", task)

    def _confirm_func(self, day, month, year, task):
        deadline = self.deadline_frame.deadline_var.get()
        if deadline:
            self.manager.edit_task(id=self.id, day=day, month=month,
                                   year=year, task=task, deadline=deadline)
        else:
            self.manager.edit_task(id=self.id,
                                   task=task, deadline=deadline)
