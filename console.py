
#Вывести на экран пять строк из нулей, количество нулей в каждой строке равно номеру строки, нули между собой разделять точкой с запятой.
def two_1():
    i = 1
    for i in range(0, 6):
        print("0;" * i)



"""
Вывести на экран букву "W" из символов "*" (звездочка). 
"""
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


