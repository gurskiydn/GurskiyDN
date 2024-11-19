peremen_1=(1,2,3,4)
peremen_2=('strochnaya')
immutable_var=(peremen_1,peremen_2)
print(immutable_var)
#peremen_1[0]=4 #выдается ошибка т.к. кортедж -не изменяемый
print(peremen_1)
print(immutable_var)
mutable_list=([1,2,3,4])
mutable_list[0]=4
print(mutable_list)