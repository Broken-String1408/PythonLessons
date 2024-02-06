stroka = 'па-ра-ра-ра ра-ра-па-па'

def rhythm(str):
    phrase = str.split()
    list_1 = []
    for word in phrase:
        vowels = 0
        for i in word:
            if i in "аеёиоуыэюя":
                vowels += 1
        list_1.append(vowels)
    return len(list_1) == list_1.count(list_1[0])

if " " not in stroka:
    print("Количество фраз должно быть больше одной!")
else:
    if rhythm(stroka):
        print("Парам пам-пам")
    else:
        print("Пам парам")

