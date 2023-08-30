from app.todo_list import TodoList
from app.interface import Todolist_interface

if __name__ == "__main__":
    todo_list = TodoList()
    app = Todolist_interface(todo_list)



