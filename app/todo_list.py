class TodoList:
    def __init__(self):
        self.tasks = []

    # ... Otros métodos ...

    def add_task(self, task_description):
        self.tasks.append(task_description)

    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_description
            return True  # Indicar éxito en la edición
        else:
            return False  # Indicar que el índice es inválido

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True  # Indicar éxito en la eliminación
        else:
            return False  # Indicar que el índice es inválido
        
    def load_tasks_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                tasks = file.readlines()
                tasks = [task.strip() for task in tasks]
                self.tasks = tasks
                return tasks
        except FileNotFoundError:
            return None

    def save_tasks_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")