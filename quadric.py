from math import*
print ("введи коэффициенты a, b, c:")
while True:
    try:
        a = float(input("a="))
        if a == 0:
            print("а не может быть равно нулю")
            continue
        b = float(input("b="))
        c = float(input("c="))
    except:
        print("Введите число")
    else: 
        break
d = b ** 2 - 4 * a * c
if d < 0: print ("корней нет")
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print ("x1=", "{:6.2f}".format(x1))
    print ("x2=", "{:6.2f}".format(x2))
