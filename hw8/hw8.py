try:
    a = input("Введите первое значение: ")
    b = input("Введите второе значение: ")
    print (a+b)
except SyntaxError:
    print(a+"str")
