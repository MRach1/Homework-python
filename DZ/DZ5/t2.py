a, b = map(int, input().split())
def suum(x, y):
    if x == 0 and y == 0:
        return 0
    elif x > 0:
        return suum(x - 1, y) + 1
    elif y > 0:
        return suum(x, y - 1) + 1
print(suum(a, b))