# Есть класс Car с атрибутами: speed (скорость), odometer (пройденное расстояние), time (время).
#     Методы:
#         accelerate() — увеличивает скорость на 5.
#         brake() — уменьшает скорость на 5.
#         step() — добавляет текущую скорость к одометру и увеличивает время на 1.
#         average_speed() — считает среднюю скорость (odometer / time).
#     В цикле программа спрашивает, что делать: ускоряться (A), тормозить (B), показать одометр (O) или среднюю скорость (S).
#
# План работы с дебагом
#
#     Поставим точки останова в ключевых местах.
#     Запустим код в дебаг-режиме.
#     Пошагово пройдёмся и посмотрим, как меняются значения.
#     Проверим на ошибки или странное поведение.
#
# Шаг 1: Подготовка в PyCharm
#
#     Скопируй код в новый файл, например car.py.
#     Поставь точки останова:
#         На строке self.speed += 5 в accelerate().
#         На строке self.odometer += self.speed в step().
#         На строке return self.odometer / self.time в average_speed().
#         Щёлкни слева от номера строки — появятся красные точки.
#
# Шаг 2: Запуск дебага
#
#     Нажми на значок жука ("Debug") вверху PyCharm или Shift + F9.
#     Программа запустится и выведет "I'm a car!", а затем спросит ввод (What should I do?).
#     Введи, например, A и нажми Enter.
#
# Шаг 3: Пошаговая отладка
#
#     Первая остановка: self.speed += 5
#         Код остановится в методе accelerate().
#         Внизу в панели отладки посмотри переменные:
#             self.speed = 0 (было до выполнения строки).
#             После нажатия F8 (Step Over) станет self.speed = 5.
#         Жми F9 (Resume), чтобы продолжить.
#     Вторая остановка: self.odometer += self.speed
#         После ввода A код дошёл до step().
#         Смотри:
#             self.speed = 5 (из accelerate).
#             self.odometer = 0 (до выполнения).
#             self.time = 0.
#         Жми F8: self.odometer станет 5, self.time станет 1.
#     Вводим S для средней скорости
#         Снова вводим S в консоли и ждём остановки на return self.odometer / self.time.
#         Смотрим:
#             self.odometer = 5.
#             self.time = 1.
#             Результат: 5 / 1 = 5. Всё верно!
#
# Шаг 4: Проверка на ошибки
#
# Давай протестируем код и найдём потенциальные проблемы с помощью дебага.
# Проблема 1: Деление на ноль
#
#     Если сразу ввести S (средняя скорость) без движения, self.time = 0, и будет ошибка ZeroDivisionError.
#     Как проверить:
#         Перезапусти дебаг (жук).
#         Введи S сразу.
#         Дойди до return self.odometer / self.time — увидишь ошибку в консоли.
#     Исправление:

def average_speed(self):
    if self.time == 0:
        return 0  # Или что-то другое, например "Машина не двигалась"
    return self.odometer / self.time

# Проблема 2: Отрицательная скорость
# Метод brake() уменьшает speed на 5, но нет проверки на отрицательное значение. Реально ли ехать назад?
# Как проверить:
#     Перезапусти дебаг.
#     Введи B несколько раз.
#     Остановись в brake() и смотри: self.speed станет -5, -10 и т.д.
# Исправление:

def brake(self):
    self.speed = max(0, self.speed - 5)  # Скорость не ниже 0

# Проблема 3: Одометр и время
#     Каждый раз после действия вызывается step(), даже если ты просто смотришь одометр (O) или скорость (S). Это логично? Может, step() нужен только при движении?
#     Как проверить:
#         Введи O и посмотри в дебаге, как self.time увеличивается в step().
#     Исправление: Перенеси my_car.step() внутрь условий A и B:

    if action == 'A':
        my_car.accelerate()
        my_car.step()
        print("Accelerating...")
    elif action == 'B':
        my_car.brake()
        my_car.step()
        print("Braking...")

# Исправленный код
# Вот как может выглядеть код после исправлений:

class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = max(0, self.speed - 5)

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time == 0:
            return 0
        return self.odometer / self.time


if __name__ == '__main__':
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
            my_car.step()
            print("Accelerating...")
        elif action == 'B':
            my_car.brake()
            my_car.step()
            print("Braking...")
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))

# Задание для тебя
#     Скопируй исправленный код в PyCharm.
#     Поставь точки останова в accelerate(), brake(), step() и average_speed().
#     Запусти дебаг и попробуй:
#         A (ускорение) → A → O (одометр) → S (средняя скорость) → B (тормоз).
#     Каждый раз смотри в панели отладки, как меняются speed, odometer и time.
