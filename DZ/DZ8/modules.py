#Ввод новой строки в файл
def Input(name, number):
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name}: {number}\n')
    print('Добавлено')


#Вывод всего файла
def OutputAll():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
       

#Поиск по имени или номеру
def Search(data):
    data = data.lower()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        F = True
        for line in file:
            if data in line.lower():
                print(line)
                F = False
        if F:
            print('\n Не найдено человека с таким именем\n')


#Удаление данных 
def Delete(name, number):
    data = name + ": " + number + "\n"
    with open("phone_book.txt", "r", encoding='utf-8') as origin:
        s = origin.readlines()
    with open("phone_book.txt", "w", encoding='utf-8') as final_version:
        for i in range(len(s)):
            if s[i] != data:
                final_version.write(s[i])


#Замена данных
def Replace(name, number, newName, newNumber):
    data = name + ": " + number + "\n"
    newData = newName + ": " + newNumber + "\n"
    with open("phone_book.txt", "r", encoding='utf-8') as origin:
        s = origin.readlines()
    with open("phone_book.txt", "w", encoding='utf-8') as final_version:
        for i in range(len(s)):
            if s[i] != data:
                final_version.write(s[i])
            else:
                final_version.write(newData)