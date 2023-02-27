point1 = "AEIOULNSTRaeioulnstrАВЕИНОРСТавеинорст"
point2 = "DGdgДКЛМПУдклмпу"
point3 = "BCMPbcmpБГЁЬЯбгёяь"
point4 = "FHVWYfhvwyЙЫйы"
point5 = "KkЖЗХЦЧжзхцч"
point8 = "JXjxШЭЮшэю"
point10 = "QZqzФЩЪфщъ"
word = input("Введите слово: ")
summ = 0
for i in word:
    if i in point1:
        summ += 1
    if i in point2:
        summ += 2
    if i in point3:
        summ += 3
    if i in point4:
        summ += 4
    if i in point5:
        summ += 5
    if i in point8:
        summ += 8
    if i in point10:
        summ += 10
print("Сумма:", summ)