a = int(input("Количество элементов в массиве: "))
s = list(map(int, input().split(maxsplit=a)))
x = int(input("Число Х: "))
raz = abs(s[0] - x)
result = 0
for i in range(a):
    if abs(s[i] - x) < raz:
        raz == abs(s[0] - x)
        result = i
print("Ближайшее число:", s[result])