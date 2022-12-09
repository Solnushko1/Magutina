def maxi(x):
    sp = []
    if x > 0:
        sp.append(x)
        return sp
    if x == 0:
        return max(sp)
print(maxi(int(input())))