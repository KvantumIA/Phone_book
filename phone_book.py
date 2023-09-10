# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def Interfeis_contact(telefon_list_name_file = 'Семинары\Seminar_Znakomstvo_Python\Seminar_8.Работа с файлами\Telefon_list.txt'):
    interfeis_contact = int(input('Введите 1 для поиска, введите 2 для добавления контакта, 3 для вывода всех контактов, 0 для выхода: '))
    while interfeis_contact != 0:
        if interfeis_contact == 1:
            Find_contact()
        elif interfeis_contact == 2:
            Write_Contact()
        else:
            Print_contacts()
        interfeis_contact = int(input('\n Введите 1 для поиска, введите 2 для добавления контакта, 3 для вывода всех контактов: '))


def Write_Contact(telefon_list_name_file = 'Семинары\Seminar_Znakomstvo_Python\Seminar_8.Работа с файлами\Telefon_list.txt'):
    with open(telefon_list_name_file, 'a', encoding='UTF-8') as telefon_list:
        first_name = input("Введите фамилию: ")        
        last_name = input("Введите имя: ")
        telefon = input("Введите телефон: ")
        while len(telefon) != 11 or not telefon.isdigit():
            print('Вы ввели неправильный телефон')
            telefon = input("Введите телефон: ")
        telefon_list.write('\n' + last_name + ', ' +  first_name + ', ' +  telefon)


def Find_contact(telefon_list_name_file = 'Семинары\Seminar_Znakomstvo_Python\Seminar_8.Работа с файлами\Telefon_list.txt'):
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        find_name = input('Поиск: ')
        lines = telefon_list.readlines()
        None_contact = True
        for i in lines:
            if find_name in i:
                print('Контакт найден:', i, end = '')
                None_contact = False
        if None_contact:
            print('Контакт не найден')


def Print_contacts(telefon_list_name_file = 'Семинары\Seminar_Znakomstvo_Python\Seminar_8.Работа с файлами\Telefon_list.txt'):
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        lines = telefon_list.readlines()
        for i in lines:
            print(i, end = '')



Interfeis_contact()