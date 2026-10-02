with open('project_td.txt', 'w', encoding = 'utf-8') as f:
    def To_do_list():
        list = []
        while True:
            task = input('(x to quit|s to see list) To do: ')
            if task.lower() == 'x':
                break
            elif task.lower() == 's':
                print('current list:', list)
            elif task.lower() == 'e':
                remove = input('Remove task: ')
                if remove in list:
                    list.remove(remove), print(f'Task "{remove}" removed.')
                else:
                    print('Task not found in list.')
            elif task.lower() == 'ccc':
                list.clear()
            else:
                list.append(task)
        return list

To_do_list()
print('To do list:', list)
content = file.read()
print('Content of the file:', content)