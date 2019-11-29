a = int(input("Enter a year: "))
def is_year_leap(a):
    if a%4 !=0 :
        return True
    else :
        return False

print(is_year_leap(a))
