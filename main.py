import tkinter as tk
from package.taskmanager.taskmanager import TaskManager
from package.gui.addtask.addtaskframe import AddTaskFrame
from package.gui.tasklist.tasklistframe import TaskListFrame

# def add():
#     global root
#     global manager
#     frame = AddTaskFrame(root, manager)


root = tk.Tk()
root.title('Task Manager')

manager = TaskManager()
# add_task_button = tk.Button(root, text='Add Task', command=add)
# add_task_button.pack()

manager.new_task(task="Neco")
manager.new_task(task="Neco")
manager.new_task(task="Neco")

print(manager.print())

menu = AddTaskFrame(root, manager)
task_list = TaskListFrame(root, manager)

root.mainloop()
