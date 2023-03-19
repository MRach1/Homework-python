import modules
while True:

    choise = int(input('Введите нужное действие: \n 1 - Добавить в справочник \
        \n 2 - Вывести всех \n 3 - Поиск по фамилии или номеру \n 4 - Удалить из справочника \n 5 - Изменить данные \n 6 - Выход \n '))
    print("\n"*40)
    match choise: 
        case 1:
            modules.Input(input('Введите имя: '), input('Введите номер: '))
        case 2: 
            modules.OutputAll()
        case 3:
            modules.Search(input('Введите фамилию или номер: '))
        case 4:
            modules.Delete(input('Введите имя и фамилию через пробел: '), input('Введите номер: '))
        case 5:
            modules.Replace(input('Введите старые имя и фамилию: '), input('Введите старый номер: '), input('Введите новое имя и фамилию: '), input('Введите новый номер: '))
        case 6: break
