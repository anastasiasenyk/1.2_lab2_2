"""json navigation"""
import json
import os.path
import time


def information(data, name):
    """
    find all dictionary keys and print them
    :param data: list/dict
    :param name: str
    :return: None
    >>> information({'a':{'b':1,'c':2}, 'd':5}, '')
    a/b
    a/c
    d
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                information(value, name + '/' + str(key))
            elif value != [] and isinstance(value, list) and isinstance(value[0], dict):
                for item in value:
                    information(item, name + '/' + str(key))
            else:
                print((name + '/' + str(key))[1:])
    elif data != [] and isinstance(data, list) and isinstance(data[0], dict):
        for item in data:
            information(item, name)


def unpacking(data, path: list):
    """
    find value by the key in dict
    :param data: list/dict
    :param path: list
    :return: str
    >>> unpacking({'a':{'b':1,'c':2}, 'd':5}, ['a', 'c'])
    '2'
    """
    if path:
        if isinstance(data, dict):
            for key, value in data.items():
                if path and str(key) == path[0]:
                    path2 = path[1:]
                    if path2:
                        new_value = unpacking(value, path2)
                        if new_value:
                            return str(new_value)
                    else:
                        return str(value)
        elif isinstance(data, list):
            for item in data:
                new_value = unpacking(item, path)
                if new_value:
                    return new_value
    return


if __name__ == '__main__':
    while True:
        print('Введіть назву файлу у вигляді /path_to_file/name_file.json')
        user = input('>>> ')
        if user == 'quit' or os.path.exists(user) and user.split('.')[-1] == 'json':
            break
        else:
            print('Ваш файл не існує або не являється файлом json.'
                  ' Cпробуйте ще раз, або введіть "quit", якщо бажаєте вийти.')

    if user != 'quit':
        try:
            with open(user, 'r') as file:
                file1 = json.load(file)
            print('Набір можливих шляхів до ключів словника')
            time.sleep(2)
        except:
            user = 'quit'
            print('Ваш файл не вдається відкрити.')

    if user != 'quit':
        information(file1, '')
        print('Введіть один із поданих ключів')
        while True:
            user = input('>>> ')
            if user != 'quit':
                if user[0] == '':
                    user = user[1:]
                value = str(unpacking(file1, user.split('/')))
            else:
                break
