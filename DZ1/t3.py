a = int(input("Номер билета: "))
sum1 = sum2 = 0
for i in range(3):
    sum1 += a%10
    a //= 10
for i in range(3):
    sum2 += a%10
    a //= 10
if sum1 == sum2:
    print("Билет счастливый")
else:
    print("Билет не является счастливым")