class CustomException1(BaseException):
    pass


class CustomException2(BaseException):
    pass


class CustomException3(BaseException):
    pass


# Создание класса с методами, выбрасывающими исключения:
class MyClass:
    def method1(self):
        if not 0 <= 5:
            raise CustomException1("Ошибка! Значение не в диапазоне")

    def method2(self):
        if not isinstance("abc", str):
            raise CustomException2("Ошибка! Некорректный тип данных")

    def method3(self):
        if {"key1": 1}.get("key2") is None:
            raise CustomException3("Ошибка! Не найден ключ")


# Класс, обрабатывающий исключения:
class ExceptionHandler:
    def processing(self, a: MyClass):
        try:
            a.method1()
            a.method2()
            a.method3()
        except CustomException1 as e:
            print(e)
        except CustomException2 as e:
            print(e)
        except CustomException3 as e:
            print(e)


# Тестирование работы класса:
handler = ExceptionHandler()
a = MyClass()

# Вызов методов класса MyClass
handler.processing(a)

# Вывод:
# Ошибка! Значение не в диапазоне
