a = float(input('ввод_длины_катета1'))
b = float(input('ввод_длины_катета2'))
c = float(input('ввод_длины_гипотенузы'))
if a ** 2 + b ** 2 == c ** 2:
    print('S=', a*b/2,'P=', a+b+c)
else: print ('error')
