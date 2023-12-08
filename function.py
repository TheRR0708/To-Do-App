FILEPATH = "todo1.txt"  # Adding in a new variable bcz of easy use


def get_todo(filepath=FILEPATH):  # directly passing the argument
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
        return todos


def write_todo(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":  #
    print("hello")
    print(get_todo())
