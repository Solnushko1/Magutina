def choco(n,m,k):
    if k < n*m and (k % m == 0 and k % n == 0):
        print("Да")
    else:
        print("Нет")
choco(int(input()), int(input()), int(input()))