import json


def get_username():
    """Имя узера"""
    filename = 'name_new.json'
    try:
        with open(filename) as f:
            user = json.load(f)

    except:
        return print("Введите Ваше имя: ")
    else: return user


def greet_user():
    """Приветсвтвие узера"""
    username = get_username()
    if username:
            print("Добро брат" + username)

    else:

        filename = 'name_new.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("Мы зап " + username)


greet_user()
