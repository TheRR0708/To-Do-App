# Adding current time and date
from hashlib import new
import time

date_time = time.strftime("%b-%d-%Y: %H-%M-%S")  # This function adding the date time function
print("It is", date_time)

import function # from module import function  ---if function file in another directory

while True:
    user_action = input("add, show, edit,complete exit:")
    user_action = user_action.strip()
    if user_action.startswith('add'):

        todo = user_action[4:]  # slicing is using here

        todos = function.get_todo()  # argument call as the filename

        todos.append(todo + '\n')  # bug fix 1 new line print

        function.write_todo(todos)

    elif user_action.startswith('show'):  # 'show' | 'dispplay' --we can use -- exp 02
        # enumarate
        todos = function.get_todo()

        # new_todos = []
        # for item in todos:    #removing the \n from the list
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos] #list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')

            # index = index + 1
            # print(index, '-' ,item)
            # f-string

            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = function.get_todo()

            new_todo = input("add new todo:")
            todos[number] = new_todo + '\n'

            function.write_todo(todos)

        except ValueError:
            print("command not found")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = function.get_todo()

            index = number - 1
            todos_to_remove = todos[index].strip('\n')

            todos.pop(index)

            function.write_todo(todos)

            meassge = f'This Todo {todos_to_remove} was removed from this list'
            print(meassge)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not valid")
print("bye!!!!")