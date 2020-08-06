from tkinter import *
from Package.taskmanager.taskmanager import TaskManager
from Package.gui.addtaskframe import AddTaskFrame

# def add():
#     global root
#     global manager
#     try:
#         frame = FrameAddTask(root, manager)
#     finally:
#         del frame

root = Tk()
root.title('Task Manager')

manager = TaskManager()
# add_task_button = Button(root, text='Add Task', command=add)
# add_task_button.pack()
menu = AddTaskFrame(root, manager)

root.mainloop()
