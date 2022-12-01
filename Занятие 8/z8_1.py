def algoritm_evklida(a, b):
    while b:
        a, b = b, a % b
    return a

a, b, c, d = map(int, input("Введите в строку A,B,C,D: ").split())

x = a * d
y = b * c
t = algoritm_evklida(x, y)

print(x // t, '/', y // t, sep='')
