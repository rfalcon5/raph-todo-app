from functions import get_todos, write_todos
import time
# import functions

user_prompt = "Type add, show, edit, complete or exit: "


now = time.strftime("%b %d, %Y %H: %M:%S")
print(now)
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()


    # Check if the user action is "add"
    if user_action.startswith('add'):
        todo = user_action[4:]



        todos = get_todos()

        todos.append(todo + '\n')

        # todo = input("Enter a Todo: ") +"\n"

        # file = open('Files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # file = open('Files/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        write_todos(todos, "todos.txt")

    elif user_action.startswith('show'):
        # file = open('Files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = get_todos('todos.txt')

        new_todos =[]

        # for item in todos:
            # new_item = item.strip('\n')
            # new_todos.append(new_item)

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index +1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos('todos.txt')
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("Files/todos.txt", todos)

        except ValueError:
            print("Your command is not Valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos('todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("Files/todos.txt", todos)

           # print(todos.pop(number -1)," has been removed!")

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is not item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        invalid_command = f"{user_action.title()} is not a valid command."
        print(invalid_command)

print("bye!")



