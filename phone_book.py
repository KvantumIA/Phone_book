# CONST
FILE_NAME = 'phone_list.txt'


def Interfeis_contact():
    interfeis_contact = int(
        input('Введите 1 для поиска, введите 2 для добавления контакта, 3 для вывода всех контактов, 0 для выхода: '))
    while interfeis_contact != 0:
        if interfeis_contact == 1:
            Find_contact()
        elif interfeis_contact == 2:
            Write_Contact()
        else:
            Print_contacts()
        interfeis_contact = int(
            input('\n Введите 1 для поиска, введите 2 для добавления контакта, 3 для вывода всех контактов: '))


def Write_Contact(phone_list_name_file=FILE_NAME):
    with open(phone_list_name_file, 'a', encoding='UTF-8') as phone_list:
        first_name = input("Введите фамилию: ")
        last_name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        while len(phone) != 11 or not phone.isdigit():
            print('Вы ввели неправильный телефон')
            phone = input("Введите телефон: ")
        phone_list.write('\n' + last_name + ', ' + first_name + ', ' + phone)


def Find_contact(phone_list_name_file=FILE_NAME):
    with open(phone_list_name_file, 'r', encoding='UTF-8') as phone_list:
        find_name = input('Поиск: ')
        lines = phone_list.readlines()
        None_contact = True
        for i in lines:
            if find_name in i:
                print('Контакт найден:', i, end='')
                None_contact = False
        if None_contact:
            print('Контакт не найден')


def Print_contacts(phone_list_name_file=FILE_NAME):
    with open(phone_list_name_file, 'r', encoding='UTF-8') as phone_list:
        lines = phone_list.readlines()
        for i in lines:
            print(i, end='')


Interfeis_contact()
