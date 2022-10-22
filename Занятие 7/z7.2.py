sp = []
new_sp = []
for n in range(10):
    sp.append(int(input()))
for i in sp:
    if i not in new_sp:
        new_sp.append(i)
print(new_sp)