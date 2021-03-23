print("Привет, ты находишься в Мирэа на развилке. Ты можешь пойти налево, направо или прямо.")
direction = input(": ")  # переменные a,b,c,d выбранные пользователем направления
if direction == "прямо":
    print("Ты поднялся на второй этаж, ты можешь пойти направо или налево, введите куда хотите пойти")
    direction2 = input(": ")
    if direction2 == "направо":
        print("Ты попал в кабинет к Арслану Тарлановичу, добро пожаловать на пару!")

    elif direction2 == "налево":
        print("тебя побили старшекурсники")
    else:
        print("Error")

elif direction == "направо":
    print("перед тобой две аудитории, справа и слева, куда пойдешь?")
    direction3 = input(":")
    if direction3 == "направо":
        print("Ты пришел на пару не в ту аудиторию")
    elif direction3 == "налево":
        print("кабинет закрыт, уходи отсюда.")
    else:
        print("Error")
elif direction == "налево":
    print("впереди кабинет ректора, зайдешь? (да или нет)")
    direction4 = input(":")
    if direction4 == "да":
        print("Тебя выгнали из кабинета")
    elif direction4 == "нет":
        print("ну ты  и трус")
    else:
        print("Error")
else:
    print("Error")
