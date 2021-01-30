
m = int(input('Введите номер задания: '))

if m == 1:
    #1
    import math
    
    H = input("Высота: ")
    R = input("Радиус: ")
    
    H = float(H)
    R = float(R)
    
    bok = math.pi*R*H
    osn = math.pi*R**2
    
    A = bok + 2*osn
    
    print ("Площадь полной поверхности: ", A)

if m == 2:
    #2
    import math
    
    R = input("Радиус: ")
    L = input("Длина: ")
    
    L= float(L)
    R = float(R)
    
    S = math.pi*(R*R)
    C = math.pi**2* R
    
    print ('Площадь круга: ', S)
    print ('Длина круга: ', C)

if m == 3:
    #3
    import math
    
    n1 = "3"
    n2 = "8"
    
    r1 = ord(n1) - ord(n2)
    r2 = ord(n1)-48 + ord(n2)-48
    
    print(r1)
    print(r2)

if m == 4:
    #4
    import math
    c = input('Буква от A до Z: ')
    
    print("Это число из: ", ord(c)-96)
    
if m == 5:
    a = input('Ваше имя? \nВведите: ')
    b = input('Какой ваш любимый предмет в школе? \nВведите: ')
    c = input('В каком классе вы учитесь? \nВведите: ')
    
    print("Ваше имя:",a , "Ваш любимый предмет:",b, "Ваш класс в школе:",c)
