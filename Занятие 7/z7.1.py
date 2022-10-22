def spisok(n):
    sp = []
    for n in range(10):
        sp.append(int(input()))
    for i in range(9): #из-за пар на 1 число меньше
        if sp[i] < 0 and sp[i+1] < 0:
            print(sp[i], sp[i+1])
spisok(1)