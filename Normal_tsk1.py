a = input('Enter int:')
b =int(a[0])
for x in range(len(a)):
    if b <= int(a[x]):
        b = int(a[x])
print(b)
