from package.taskmanager.taskmanager import TaskManager
from package.gui.mainwindow.mainwindow import MainWindow


manager = TaskManager()
root = MainWindow(manager)

manager.new_task(11, 11, 2020, task="Neco")
manager.new_task(1, 2, 2022, task="Neco")
manager.new_task(task="Neco")


root.mainloop()

# edit
