

def show_instructions():
    print('Нажмите -1- для показа всего справочника\n'
          'Нажмите -2- для добавления нового номера\n'
          'Нажмите -3- для поиска по номеру\n'
          'Нажмите -4- для удаления номера')

def user_command():
    print('Введите номер команды от 1 до 4: ', end = '')
    return int(input())
