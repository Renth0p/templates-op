import math

task = int(input('Введите номер задания: '))

if task == 1:
    
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))
    if a > b > c:
        print (math.sin(a))
    elif b > a > c:
        print (math.sin(b))
    else:
        print (math.sin(c))
        
if task == 2:
    a = int(input('Введите число: '))
    if a % 2 == 0:
        print('Четное число')
    else:
        print('Нечентное число')
        
if task == 3:
    a = 6
    b = 6
    c = 4
    
    if a>b:
        if a>c:
            y=a
        else:
            y=c
    else:
        if b>c:
            y=b
        else:
            y=c
            
    print('Максимальное: ', y) 
    
if task == 4:
    a = 143
    b = 14
    
    if a%b == 0:
        print("Делится")
    else:
        print("не делится. Oстаток:", a%b)
        
