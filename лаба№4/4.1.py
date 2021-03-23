while True:
    password = input(":")
    if len(password) < 8:
        print("Пароль короткий!")
    elif "123" in password:
        print("Пароль простой!")
    else:
        password2 = input(":")
        if password2 == password:
            print("OK")
            break
        else:
            print("Пароли не совпадают")
