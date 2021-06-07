'''#первое задание
print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
#втарое задание
a = 10
b = 20
c = 30
A = a + b
B = c - a
C = a + b + c
print(A, B, C)


#третье задание 
a = int(input("введите сторону квадрата"))
print(a * 4)





#задача 5
i = 0
while i < 300:
	print(i)
	i+=2
'''

#задача 6
import random as rd
i=0
while i < 3:
    random_number = rd.randint(0,10)
    a = input("введите число")
    print(random_number)
    if random_number == a:
    	print("вы выиграли")
    else:
    	print("вы проиграли")
    i+=1
    '''q
#задача 7
a = input("введите слово из шести")
b = tuple(a)
d = len(a)
while d < 6:
	a = input("введите слово из шести букв")
    print(b)
'''