def is_prime(a):
    if a%a == 0 and a%1 ==0 :
        return True
    else :
        return False
n = int(input("Введите число: "))
print(is_prime(n))
