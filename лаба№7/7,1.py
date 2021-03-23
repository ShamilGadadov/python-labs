x=int(input(":"))
i=1
while i<=x:
    i+=1
    y=input(":")
    if 'Cat' in y or 'cat' in y:
        print('MIAOW')
    else:
        print('NO CAT')