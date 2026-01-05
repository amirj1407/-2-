users = []


def find_user(login):
    for user in users:
        if user["login"] == login:
            return user
    return None


def register_user(login, password):
    if find_user(login) is not None:
        return False
    users.append({
        "login": login,
        "password": password
    })
    return True


def login_user(login, password):
    user = find_user(login)
    if user is None:
        return False
    if user["password"] != password:
        return False
    return True


def show_users():
    return users


def main_menu():
    print("1 — Регистрация")
    print("2 — Вход")
    print("3 — Показать пользователей")
    print("0 — Выход")


while True:
    main_menu()
    choice = input("Выбери действие: ")

    if choice == "1":
        login = input("Логин: ")
        password = input("Пароль: ")
        if register_user(login, password):
            print("Пользователь создан")
        else:
            print("Такой пользователь уже есть")

    elif choice == "2":
        login = input("Логин: ")
        password = input("Пароль: ")
        if login_user(login, password):
            print("Вход выполнен")
        else:
            print("Ошибка входа")

    elif choice == "3":
        print(show_users())

    elif choice == "0":
        break