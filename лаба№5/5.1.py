a = int(input(":"))
summ = 1
h = 0
while h != a:
    if summ * 2 < a:
        summ *= 2
    else:
        summ += 1
    h += 1
print(h, summ)