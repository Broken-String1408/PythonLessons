# dir_ks = {"АВЕИНОРСТAEIOULNSTR" : 1, 
#        "ДКЛМПУDG" : 2, 
#        "БГЁЬЯBCMP" : 3, 
#        "ЙЫFHVWY" : 4,
#        "ЖЗХЦЧK" : 5, 
#        "ШЭЮJX" : 8, 
#        "ФЩЪQZ" : 10}
# key = [1, 2, 3, 4, 5, 8, 10]
# val
# k = input("ВВедите слово: ").upper()
# res = 0
# for i in k:
#     for key, val in dir_ks.items():
#         if i in val:
#             res += key
# print(res)


k = "ноутбук"
k = str.upper(k)
key = [1, 2, 3, 4, 5, 8, 10]
value = ['AEIOULNSTRАВЕИНОРСТ', 'DGДКЛМПУ', 'BCMPБГЁЬЯ', 'FHVWYЙЫ', 'KЖЗХЦЧ', 'JXШЭЮ', 'QZФЩЪ']
dict = {k:v for k, v in zip(key, value)}

# Вариант 2 задания словаря: 
dict = {1:"AEIOULNSTRАВЕИНОРСТ", 2:"DGДКЛМПУ", 3:"BCMPБГЁЬЯ", 4:"FHVWYЙЫ", 5:"KЖЗХЦЧ", 8:"JXШЭЮ", 10:"QZФЩЪ"}

sum = 0

for i in k:
    for key, val in dict.items():
        if i in val:
            sum += key

print(f'Стоимость слова {k}: {sum}')



# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)
