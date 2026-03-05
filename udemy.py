counts = 0

b = {'1': 'Камень', '2': 'Ножницы', '3': 'Бумага'}
print('              Добро пожловать\n Это игра "Камень, ножницы, бумага» (на 2 игрока)"')
print()
print('Правило:\nКамень-Ножницы, Ножницы-Бумага, Бумага-Камень')
sas = input('Ведите сколько раз хотите сыграть; ')

while counts < int(sas):

    user1 = input('Напишите имя (1игрок):   ').capitalize()
    user2 = input('Напишите имя (2 игрок):   ').capitalize()

    print(f'{user1} Ваш противник {user2}')

    user11 = input(f'{user1} Выберите "1-Камень, 2-ножницы, 3-бумага»')

    if user11.capitalize() in b.keys():
        print('\n' * 2)
    else:
        print('Вы велли не коректно')
    user22 = input(f'{user2} Выберите "1-Камень, 2-ножницы, 3-бумага»')
    if user22.capitalize() in b.keys():
        print('\n')
    else:
        print('Вы велли не коректно')

    if (user11 == '1' and user22 == '2') or (user11 == '2' and user22 == '3') or (user11 == '3' and user22 == '1'):
        print(f"Победил {user1}!")
        print(f'{user1} Выбрал - {b[user11]}')
        print(f'{user2} Выбрал - {b[user22]}')
        counts += 1
    elif (user22 == '1' and user11 == '2') or (user22 == '2' and user11 == '3') or (user22 == '3' and user11 == '1'):
        print(f"Победил {user2}!")
        print(f'{user2} Выбрал - {b[user22]}')
        print(f'{user1} Выбрал - {b[user11]}')
        counts += 1
    else:
        print('Ничья')
    print(f'Это была {counts} игра')


