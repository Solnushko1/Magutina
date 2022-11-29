#запись матрицы в массив
def yupi(x):
    matrica = []
    i = 0
    j = 0
    print("Заполните матрицу своими значениями:")
    matrica = [[0 for _ in range(x)] for _ in range(x)]
    for i in range(x):
        matrica[i][i] = int(input())
        for j in range(i + 1, x):
                matrica[i][j] = int(input())
                matrica[j][i] = matrica[i][j]
    return matrica

def zapis_v_fail(m):
    with open("C:\\Users\\My\\PycharmProjects\\pythonProject\\Основы\\lesson 10\\ex1.txt", "w") as f:
        for line in m:
            for el in line:
                f.write(str(el) + " ")
            f.write('\n')

n = int(input("Введите значение N:"))
m = int(input("Введите значение M:"))
a = n * m
print("Размер матрицы:", a)

x = yupi(a)
zapis_v_fail(x)