weather = int(input("Температура за окном: "))
if weather == -30 :
    print ("Там так холодно,лучше дома сиди")
elif weather >-30 and weather <= 0:
    print ("Холодновато,Оденься теплее")
elif weather >0 and weather < 15 :
    print ("Прохладно,Куртку накинь")
elif weather >= 15 and  weather <= 30 :
    print ("Тепло.Иди погуляй в парке")
elif weather > 30 and weather <= 50 :
    print ("Ого.Как жарко")
elif weather > 50:
    print ("Такая жара.Лучше сиди дома")
else :
    print ("Ошибка")
