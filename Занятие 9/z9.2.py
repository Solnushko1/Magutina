from random import randint
def yupi(n,m,max_znach):
    a = [[randint(0, max_znach) for i in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if a[i][j] % 2 == 0:
                a[i][j] = 0
            else:
                a[i][j] = 1
    for i in range(m):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
yupi(int(input('Введите n:')),int(input('Введите m:')),int(input('Введите максимальую цифру:')))