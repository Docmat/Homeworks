# Тернарный оператор - присвоение значений переменной через условие
my_list = [1,2,3,4,5]
my_list2 = [5,6,7,8,9]
my_list3 = list(map(lambda x,y: x+y , my_list,my_list2))
print(my_list3)
