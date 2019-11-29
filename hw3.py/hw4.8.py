password_list = ['password', '12 3456', '12345678', 'qwerty', 'abc 123', 'monkey', '12234567']
while True:
    a = input("Enter a password: ")
    if a in password_list:
        print ("Password is correct")
        break
    else:
        continue
