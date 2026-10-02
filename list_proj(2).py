#Try to load existing tasks from a text file.
tasks = []
try:
    with open('tasks.txt', 'r') as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass  #File will be created automatically when saving. Lowkey ion undertsand ts that much

while True:
    print('--- TO-DO LIST ---')

    #Display current list
    if len(tasks) == 0:
        print('Your list is empty.')
    else:
        number = 1
        for task in tasks:
            print(str(number) + '. ' + task)
            number = number + 1

    #menu options
    print('What would you like to do?')
    print('1. Add a task')
    print('2. Delete a task')
    print('3. Quit')

    choice = input('Enter 1, 2, or 3: ')

    #Add task
    if choice == '1':
        new_task = input('Type your task: ')
        tasks.append(new_task)
        print("Task added!")

    #Del task
    elif choice == '2':
        task_num = input('Enter the number of the task to delete: ')
        if task_num.isdigit():
            index = int(task_num) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                print('Task deleted!')
            else:
                print('That task number does not exist.')
        else:
            print('Please enter a number.')

    #Quit
    elif choice == '3':
        print('Goodbye!')
        break

    else:
        print('Invalid option, please choose 1, 2, or 3.')

    #Save list (txt file)
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')