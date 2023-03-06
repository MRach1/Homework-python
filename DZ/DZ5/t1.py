a = int(input("Число: " ))
b = int(input("Степень: " ))
def f(x, y):
    if y <= 0:
        return 1
    else:
        return f(x, y - 1) * x
print(f(a, b))