glas = "EYUIOAeyuioaУЕЫАОИЭЯЮуеыаоэяию"
strr = list(input().split())
gl = len(list(filter(lambda x: x in glas, strr[0])))
F = True
for i in strr:
    if len(list(filter(lambda x: x in glas, i))) != gl:
        F = False
        break
if F:
    print("Парам пам-пам")
else:
    print("Пам парам")

