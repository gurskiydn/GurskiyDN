from idlelib.debugobj import myrepr

my_dict={"Dima":9647964444,"Oxana":9067215555,"Sergey":9687778877}#создал словарь
print(my_dict)
print(my_dict["Dima"])#вывод на экран по 1му ключу
my_dict["Lena"]=9031788888
print(my_dict)
a={"Kolya":9164167777,"Natashf":8916234567}
my_dict.update({"Dasha":9057019999,"Tanya":9161354311})
print((my_dict))
my_dict.update(a)
print(my_dict)
a = my_dict.pop("Oxana")
print(my_dict)
print(a)#вывод по удаленному ключу
my_set={1,1,2,3,4,2,5.123,3,"metod"}
print(my_set)
print(my_set.add(45))#добавление элемента
print(my_set)
print(my_set.discard(3)) #удаление элемента
print(my_set)