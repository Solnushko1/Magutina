#задание 1 из блока Б
def maxi(x):
    max_elem = 0
    while x != 0:
        if x > max_elem:
           max_elem = x
        x = int(input())
    return max_elem
print(maxi(int(input())))