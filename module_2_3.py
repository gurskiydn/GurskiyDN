from sys import breakpointhook

my_list = [42 , 69  , 322 , 13 , 0 , 99 , -5 , 9 , 8 , 7 , -6 , 5]
kol_sim = len(my_list)
a = 0 # Начальный символ
while kol_sim > a:
    chislo = (my_list[a])
    if chislo < 0:
        break
        print(chislo)
    elif  chislo >0 :
        print(chislo)
    a = a + 1



