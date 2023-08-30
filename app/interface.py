import tkinter as tk
from .todo_list import TodoList

class Todolist_interface:
    def __init__(self, todo_list_instance):
        self.todo_list = todo_list_instance
        self. window = tk.Tk()
        self.window.title("ToDo List")

        self.add_widget()
        self.add_buttons()

        self.window.mainloop()

    def add_widget(self):
         self.task_listbox = tk.Listbox(self.window, width=50, height=10)
         self.task_listbox.pack()

    def add_buttons(self):
        self.add_button = tk.Button(self.window, text="Agregar Tarea", command=self.add_task_window)
        self.add_button.pack(fill=tk.X, pady=5)

        self.edit_button = tk.Button(self.window, text="Editar Tarea", command=self.edit_task)
        self.edit_button.pack(fill=tk.X, pady=5)

        self.delete_button = tk.Button(self.window, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(fill=tk.X, pady=5)

        self.load_button = tk.Button(self.window, text="Cargar Tareas", command=self.load_tasks)
        self.load_button.pack(fill=tk.X, pady=5)

        self.save_button = tk.Button(self.window, text="Guardar Tareas", command=self.save_tasks)
        self.save_button.pack(fill=tk.X, pady=5)

    def add_task_window(self):
        top = tk.Toplevel(self.window)  # Crea una ventana emergente
        top.title("Agregar Tarea")

        task_label = tk.Label(top, text="Descripción de la tarea:")
        task_label.pack()

        task_entry = tk.Entry(top)
        task_entry.pack()

        add_button = tk.Button(top, text="Agregar", command=lambda: self.add_task(task_entry.get(), top))
        add_button.pack()

    def add_task(self, task_description, top):
        if task_description:
            self.todo_list.add_task(task_description)
            self.update_task_listbox()
            top.destroy() 
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, task)
        

    def edit_task(self):
        pop = tk.Toplevel(self.window)  
        pop.title("Editar tarea")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if self.todo_list.delete_task(index):
                self.update_task_listbox()

    def load_tasks(self):
        tasks = self.todo_list.load_tasks_from_file("tasks.txt")
        if tasks:
            self.update_task_listbox()

    def save_tasks(self):
        self.todo_list.save_tasks_to_file("tasks.txt")