'''i = 0
while i < 1000:
	a = i
	i+=3
i = 0
while i < 1000:
	b = i
	i+=5
s = a + b
print(s)




a = 333
b = 555
a,b = b,a
print(a, b)


for i in range(0,1000):
	if i % 3 == 0:
		for a in range(0,1000):  
		    if a % 5 == 0:
			    s = a + i
			    print(s)





date = {}
a = input("введите дату")
print(a)
b = date.append(a)
print(b)








#пятое задание
один = 1
a = один + один + один + один + один
print(a)
b = один * 7
print(b)






list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = list_2.set(list_1)
print(a)




my_friends = {
    "Joomart": "+996555246810",
    "Adinai": "+996555013579",
    "Ermek": "+996777013579",
    "Atai": "+996777246810",
    "Aslan": "+996999246810"}

his_her_friends = {
    "Lyazat": "+996551123456",
    "Salavat": "+996552234567",
    "Daniyar": "+996553345678",
    "Bolot": "+996554456789",
    "Alymbek": "+996555501234",
    "Dastan": "+996556678912",
    "Maksat": "+996557789012",
    "Aibek": "+996558890123",}
our_friends = {}
his_her_friends.append(my_friends)
print(my_friend)

'''



'''
b = int(input("введите ваш вес"))
if b < 50: 
    print("вам нужно набрать вес")
    d = 50 - b
    print(d, "кг веса вам нехватет")
elif b > 80:
    print("вам нужно сбросить вес")
    g = b - 80 
    print(g, "кг вам нужно сбросить")
else:
    print("у вас правильный вес")

a = int(input("введите ваш рост"))   
if a < 150:
	print("вы низкий")
elif a > 170:
	print("вы высокий")
else:
	print("у вас средний рост")
'''


#Тут всё просто, достаточно сравнить строку с её 
#обратной версией, для чего можно использовать 
#встроенную функцию reversed:
words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопк    у',]
def is_palindrome(string):
    return string == ''.join(reversed(string))
print(is_palindrome(words))
#Того же эффекта можно добиться с помощью срезов:





