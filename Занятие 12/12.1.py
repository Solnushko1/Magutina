#задание 2 из блока А
def delenie(a,b):
    if a >= b:
        return delenie(a-b, b)
    else:
        return a
print(delenie(int(input()),int(input())))