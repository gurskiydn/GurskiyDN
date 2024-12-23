def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() # вызов функции внутри test_function
test_function()
inner_function() #При попытке вызвать inner_function вне test_function возникает ошибка, потому что inner_function
# не доступна за пределами своей области видимости.
