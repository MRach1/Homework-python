a = int(input("Количество элементов в массиве: "))
s = list(map(int, input().split(maxsplit=a)))
x = int(input("Число Х: "))
print(f"Число {x} встречается {s.count(x)} раз(a)")
