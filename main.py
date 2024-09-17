# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
from unittest import result
import random



#Вывести на экран пять строк из нулей, количество нулей
# в каждой строке равно номеру строки, нули между собой разделять точкой с запятой.
def two_1 ():
    i = 1
    for i in range(0, 6):
        print("0" * i)
#(x+1)2+3(x+1) при x =1.7.
def math_two():
    x = 1.7  # Присваиваем значение переменной x
    result = (x + 1) ** 2 + 3 * (x + 1)  # Вычисляем выражение
    print(result)  # Выводим результат
def eight():
    rect_width = 647
    rect_height = 170
    square_side = 30

    # Рассчитаем количество квадратов по ширине и высоте
    squares_per_width = rect_width // square_side
    squares_per_height = rect_height // square_side

    # Общее количество квадратов
    total_squares = squares_per_width * squares_per_height

    # Форматированный вывод
    print(
        f"Прямоугольник размером {rect_width}x{rect_height} "
        f"вмещает {total_squares} квадратов со стороной {square_side}."
    )
def print_w():
    height = 4
    for i in range(height):
        if i == 0:
            print("*     *     *")
        elif i == 1:
            print(" *   * *   * ")

        elif i == 2:
            print("  * *   * *  ")
        elif i == 3:
            print("   *     *   ")
def math_fore(a):
    # a^2 за 1 операцию
    a2 = a * a
    # a^4 за 2 операции
    a4 = a2 * a2
    # a^6 за 3 операции
    a6 = a4 * a2
    # a^3 за 2 операции (нужно для a^15)
    a3 = a2 * a
    # a^6 уже посчитано (3-я операция), a^12 за 4 операции
    a12 = a6 * a6
    # a^15 за 5 операций
    a15 = a12 * a3

    return a4, a6, a15
def math_six():
    # Ввод данных от пользователя
    principal = float(input("Введите начальную сумму вклада: "))
    annual_rate = float(input("Введите годовой процент: "))
    years = 5  # В данном случае фиксированное количество лет

    # Вычисление суммы вклада через 5 лет
    future_value = principal * (1 + annual_rate / 100) ** years

    print(f"Сумма вклада через {years} лет составит: {future_value:.2f}")
def opiration_2():
    # Ввод четырех чисел от пользователя
    try:
        numbers = [int(input(f"Введите число {i + 1}: ")) for i in range(4)]

        # Фильтрация четных чисел
        even_numbers = [num for num in numbers if num % 2 == 0]

        # Поиск наибольшего четного числа
        if even_numbers:
            largest_even = max(even_numbers)
            print(f"Наибольшее четное число: {largest_even}")
        else:
            print("Четные числа не найдены")
    except ValueError:
        print("Пожалуйста, введите корректное число")
def check_date():
    # Запрашиваем у пользователя день, месяц и год и преобразуем их в целые числа
    day = int(input("Введите день: "))
    month = int(input("Введите месяц: "))
    year = int(input("Введите год: "))

    # Создаем словарь, в котором хранятся количество дней в каждом месяце
    # Например, в месяце 1 (январь) 31 день, в месяце 2 (февраль) 28 дней и так далее
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Проверяем, что введенный месяц находится в допустимом диапазоне от 1 до 12
    # Если месяц меньше 1 или больше 12, выводим "no" и прекращаем выполнение функции
    if month < 1 or month > 12:
        print("no")
        return

    # Проверяем, что введенный день находится в допустимом диапазоне для указанного месяца
    # Если день меньше 1 или больше количества дней в указанном месяце, выводим "no" и прекращаем выполнение функции
    if day < 1 or day > days_in_month[month]:
        print("no")
        return

    # Попытка создать объект даты с помощью класса datetime
    # Если дата корректна, то объект успешно создастся, и мы выведем "yes"
    # Если дата некорректна (например, 30 февраля), то будет вызвано исключение ValueError
    # В этом случае выводим "no"
    try:
        datetime(year, month, day)
        print("yes")
    except ValueError:
        print("no")
def fivenumber():
    number = input("Ведите число: ")

    if len(number) != 5:
        return "Ошибка: число должно быть пятизначным"

    result = []

    for i, digit in enumerate(number):
        if i % 2 == 0:
            result.append('0')
        else:
            result.append(digit)

# преобразую список, где хранятся данные в строку для вывода
    print(''.join(result))

# Общая функция для определения принадлежности и пересечения прямоугольников
def check_rectangles():
    # Запрашиваем координаты и размеры первого прямоугольника
    print("Введите координаты левого нижнего угла и размеры первого прямоугольника:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    w1 = float(input("Ширина первого прямоугольника: "))
    h1 = float(input("Высота первого прямоугольника: "))

    # Запрашиваем координаты и размеры второго прямоугольника
    print("Введите координаты левого нижнего угла и размеры второго прямоугольника:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    w2 = float(input("Ширина второго прямоугольника: "))
    h2 = float(input("Высота второго прямоугольника: "))

    # Проверка, принадлежат ли все точки первого прямоугольника второму
    rect1_in_rect2 = (x1 >= x2 and y1 >= y2 and (x1 + w1) <= (x2 + w2) and (y1 + h1) <= (y2 + h2))

    # Проверка, принадлежат ли все точки второго прямоугольника первому
    rect2_in_rect1 = (x2 >= x1 and y2 >= y1 and (x2 + w2) <= (x1 + w1) and (y2 + h2) <= (y1 + h1))

    # Проверка пересечения прямоугольников
    intersect = not (x1 + w1 <= x2 or x1 >= x2 + w2 or y1 + h1 <= y2 or y1 >= y2 + h2)

    # Вывод результатов
    print(f"Все точки первого прямоугольника принадлежат второму: {rect1_in_rect2}")
    print(f"Все точки второго прямоугольника принадлежат первому: {rect2_in_rect1}")
    print(f"Прямоугольники пересекаются: {intersect}")

def dollar_to_rubles_table():
    # Запрос курса доллара
    dollar_rate = float(input("Введите курс доллара в рублях: "))
    candy_price_kg = 20.0  # Цена 1 кг конфет в рублях

    # Вывод заголовков таблицы
    print(f"{'Доллары':<10}{'Рубли':<10}{'Кг конфет':<10}")
    print("-" * 30)

    # Вычисляем и выводим для каждого значения от 1 до 100 долларов
    for dollars in range(1, 101):
        rubles = dollars * dollar_rate  # Сумма в рублях
        candies = rubles / candy_price_kg  # Количество килограммов конфет
        print(f"{dollars:<10}{rubles:<10.2f}{candies:<10.2f}")

def print_square():
    size = 10

    for i in range(size):
        for j in range(size):
            if i == j:
                print(0, end=" ")  # Нули на диагонали
            else:
                print(1, end=" ")  # Единицы вне диагонали
        print()  # Переход на новую строку

def count_even_numbers():
        count = 0  # Счетчик четных чисел
        while True:
            num = int(input("Введите целое число (0 для завершения): "))
            if num == 0:
                break  # Прерываем цикл, если введен 0
            if num % 2 == 0:
                count += 1  # Увеличиваем счетчик, если число четное
        print(f"Количество четных чисел: {count}")


# Варианты ходов (список возможных ходов для игры "Камень, Ножницы, Бумага")
moves = ['Камень', 'Ножницы', 'Бумага']


# Функция для игры
def play_rps():
    # Количество раундов, которое пользователь хочет сыграть
    n = int(input("Сколько игр вы хотите сыграть? "))

    # Инициализация переменных для подсчета побед и ничьих
    user_wins = 0  # количество побед пользователя
    computer_wins = 0  # количество побед компьютера
    draws = 0  # количество ничьих

    # Словари для хранения количества выборов каждого хода пользователем и компьютером
    user_choices = {'Камень': 0, 'Ножницы': 0, 'Бумага': 0}
    computer_choices = {'Камень': 0, 'Ножницы': 0, 'Бумага': 0}

    # Функция для выбора хода компьютера
    def computer_move():
        # Анализ частоты ходов пользователя: компьютер выбирает ход, который побеждает наиболее частый выбор пользователя
        if user_choices['Камень'] > user_choices['Ножницы'] and user_choices['Камень'] > user_choices['Бумага']:
            return 'Бумага'  # Бумага бьет Камень
        elif user_choices['Ножницы'] > user_choices['Камень'] and user_choices['Ножницы'] > user_choices['Бумага']:
            return 'Камень'  # Камень бьет Ножницы
        elif user_choices['Бумага'] > user_choices['Камень'] and user_choices['Бумага'] > user_choices['Ножницы']:
            return 'Ножницы'  # Ножницы бьют Бумагу
        else:
            return random.choice(moves)  # Если у пользователя нет доминирующего хода, компьютер выбирает случайно

    # Основной цикл игры (n раундов)
    for i in range(n):
        print("\nИгра", i + 1)  # выводим текущий номер раунда
        print("Выберите ваш ход:")
        print("1 - Камень")
        print("2 - Ножницы")
        print("3 - Бумага")

        # Получаем выбор пользователя
        user_input = int(input("Ваш выбор (1/2/3): "))
        if user_input not in [1, 2, 3]:  # проверяем, правильный ли ввод
            print("Неправильный ввод, попробуйте снова.")
            continue  # если ввод неправильный, просим повторить

        user_move = moves[user_input - 1]  # преобразуем выбор пользователя в строку ("Камень", "Ножницы", "Бумага")
        user_choices[user_move] += 1  # обновляем статистику ходов пользователя

        comp_move = computer_move()  # компьютер делает свой ход
        computer_choices[comp_move] += 1  # обновляем статистику ходов компьютера

        print(f"Ваш ход: {user_move}")
        print(f"Ход компьютера: {comp_move}")

        # Определение результата раунда
        if user_move == comp_move:
            print("Ничья!")
            draws += 1  # если ходы совпали, это ничья
        elif (user_move == 'Камень' and comp_move == 'Ножницы') or \
                (user_move == 'Ножницы' and comp_move == 'Бумага') or \
                (user_move == 'Бумага' and comp_move == 'Камень'):
            print("Вы выиграли!")
            user_wins += 1  # если пользователь выиграл, увеличиваем счетчик его побед
        else:
            print("Компьютер выиграл!")
            computer_wins += 1  # если компьютер выиграл, увеличиваем счетчик побед компьютера

    # Вывод статистики по завершении всех раундов
    print("\n--- Статистика ---")
    print(f"Победы пользователя: {user_wins}")
    print(f"Победы компьютера: {computer_wins}")
    print(f"Ничьи: {draws}")

    # Вывод количества выборов каждого хода пользователем и компьютером
    print("\nХоды пользователя:")
    for move, count in user_choices.items():
        print(f"{move}: {count}")

    print("\nХоды компьютера:")
    for move, count in computer_choices.items():
        print(f"{move}: {count}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
       #two_1()
    #print_w()
     #  math_two()
     #  eight()
   # print(math_fore(2))
     #  math_six()
        #opiration_2()
      # check_date()
    #  fivenumber()
       #check_rectangles()
     #  dollar_to_rubles_table()
       #print_square()
       #count_even_numbers()
       play_rps()








