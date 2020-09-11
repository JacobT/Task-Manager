from package.taskmanager import taskmanager
from package.gui.mainwindow import mainwindow


manager = taskmanager.TaskManager()
root = mainwindow.MainWindow(manager)

root.mainloop()
