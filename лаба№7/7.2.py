nol = int(input(":"))
for i in range(nol):
    txt = input(":")
    if txt.lower().find('кот') >= 0:
        print('МЯУ')
        break
else:
    print('НЕТ')