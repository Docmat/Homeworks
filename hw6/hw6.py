import shutil

# Первое задание
file = open("kyrgyzstan.txt", "w")
writer = file.write("Kyrgyzstan, country of Central Asia.It is bounded by Kazakhstan on the northwest and north, by China on the east and south, and by Tajikistan and Uzbekistan on the south and west. Most of Kyrgyzstan’s borders run along mountain crests. The capital is Bishkek (known from 1862 to 1926 as Pishpek and from 1926 to 1991 as Frunze")
file.close()

file = open ("kyrgyzstan.txt", "r")
print(str(len(file.read())))
file.close()
#второй способ
with open("kyrgyzstan.txt", "r") as data :
    print(len(data.read()))

# Второе задание
shutil.copy("kyrgyzstan.txt", "wikipedia.txt")
file = open("wikipedia.txt","a")
file.write("\nThe Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991.")
file.close()

#второй способ
with open("wikipedia.txt","a") as a:
    a.write("The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991")