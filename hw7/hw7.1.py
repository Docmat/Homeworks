
month = int(input("Choose a month : "))
def season(month):

    if month < 3 or month  == 12:
        return "Winter"
    elif 3 <= month < 6:
        return "Spring"
    elif 6 <= month < 9:
        return "Summer"
    elif 9 <= month < 12:
        return "Autumn"
    else :
        return False

print(season(month))
