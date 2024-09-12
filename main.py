# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Вывести на экран пять строк из нулей, количество нулей
# в каждой строке равно номеру строки, нули между собой разделять точкой с запятой.
def two_1 ():
    i = 1
    for i in range(0, 6):
        print("0" * i)
#(x+1)2+3(x+1) при x=1.7.
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
        largest_even = max(even_ginumbers)
        print(f"Наибольшее четное число: {largest_even}")
    else:
        print("not found")






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
       #two_1()
    #print_w()
     #  math_two()
     #  eight()
   # print(math_fore(2))
     #  math_six()
        opiration_2()








