import tkinter as tk

class Todolist_interface:
    def __init__(self):
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
        self.add_button.pack(pady=5)

    def add_task_window(self):
        top = tk.Toplevel(self.window)  # Crea una ventana emergente
        top.title("Agregar Tarea")