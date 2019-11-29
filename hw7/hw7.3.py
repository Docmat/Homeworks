a = int(input("Введите первое число: "))
b = int(input ("Введите второе число: "))
c = str(input ("Введите знак операции: "))
def arithmetic(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    else:
        return "Неизвестная операция"
print(arithmetic(a,b,c))
