import tkinter as tk
from tkinter import Label, Entry, Button, Listbox, Scrollbar, END, messagebox
from task import Task
from scheduler import Scheduler

class SchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Scheduler")

        # Initialize the tasks list
        self.tasks = []

        # Task input fields
        Label(root, text="Task ID:").grid(row=0, column=0)
        self.task_id = Entry(root)
        self.task_id.grid(row=0, column=1)

        Label(root, text="Period:").grid(row=1, column=0)
        self.task_period = Entry(root)
        self.task_period.grid(row=1, column=1)

        Label(root, text="Deadline:").grid(row=2, column=0)
        self.task_deadline = Entry(root)
        self.task_deadline.grid(row=2, column=1)

        Label(root, text="Execution Time:").grid(row=3, column=0)
        self.task_execution_time = Entry(root)
        self.task_execution_time.grid(row=3, column=1)

        Label(root, text="Start Time:").grid(row=4, column=0)
        self.task_start_time = Entry(root)
        self.task_start_time.grid(row=4, column=1)

        # Buttons for operations
        Button(root, text="Add Task", command=self.add_task).grid(row=5, column=0)
        Button(root, text="Run RMS", command=lambda: self.run_scheduler('RMS')).grid(row=5, column=1)
        Button(root, text="Run EDF", command=lambda: self.run_scheduler('EDF')).grid(row=5, column=2)
        Button(root, text="Exit", command=root.destroy).grid(row=6, column=1)

        # Display for tasks
        self.task_list = Listbox(root, height=10, width=50)
        self.task_list.grid(row=7, column=0, columnspan=3)
        scrollbar = Scrollbar(root, command=self.task_list.yview)
        scrollbar.grid(row=7, column=3, sticky='nsew')
        self.task_list.config(yscrollcommand=scrollbar.set)

    def add_task(self):
        # Function to add tasks to the Listbox and task list
        id = self.task_id.get()
        periodo = int(self.task_period.get())
        deadline = int(self.task_deadline.get())
        tiempo_ejecucion = int(self.task_execution_time.get())
        tiempo_inicio = int(self.task_start_time.get())
        tarea = Task(id, periodo, deadline, tiempo_ejecucion, tiempo_inicio)
        self.tasks.append(tarea)
        self.task_list.insert(END, f"ID: {id}, Period: {periodo}, Deadline: {deadline}, Exec Time: {tiempo_ejecucion}, Start: {tiempo_inicio}")
        messagebox.showinfo("Task Added", f"Task {id} added successfully.")

    def run_scheduler(self, mode):
        # Modified run_scheduler as above
        if not self.tasks:
            messagebox.showinfo("No Tasks", "Please add tasks before running the scheduler.")
            return

        self.scheduler = Scheduler(mode=mode)
        for task in self.tasks:
            self.scheduler.agregar_tarea(task)
        self.scheduler.ejecutar()
        results = "\n".join(self.scheduler.log)
        messagebox.showinfo(f"{mode} Results", results)
        self.tasks.clear()
        self.task_list.delete(0, END)
        self.scheduler.log = []

# Usage
if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerGUI(root)
    root.mainloop()
