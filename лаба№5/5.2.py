print('ВВЕДИТЕ КОЛИЧЕСТВО КАМНЕЙ')
print('-------------------------')
one = int(input('Первой кучи: '))
two = int(input('Второй кучи: '))

bunch = 0
taken = 0

while True:
    bunch = int(input('Введите номер кучи - из которой беруться камни: '))
    taken = int(input('Введите количество забираемых камней: '))

    if bunch == 1:
        if one - taken >= 0:
            one -= taken
    else:
        if two - taken >= 0:
            two -= taken

    if one == 0 or two == 0:
        break

    print("Осталось количество камней первой кучи {o}, второй {t}".format(o=one, t=two))