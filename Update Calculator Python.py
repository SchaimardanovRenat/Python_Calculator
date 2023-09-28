import math
def sum_numbers(first_number, second_number):
    return first_number + second_number
def defference_numbers(first_number, second_number):
    return first_number - second_number
def divide_numbers(first_number, second_number):
    try:
        result = first_number / second_number
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль недопустимо!")
def multiply(first_number, second_number):
    return  first_number ** second_number


def is_even(first_number):
    if first_number % 2 == 0:
        return True
    else:
        return False
def sum_digits(first_number):
    if first_number < 10:
        return first_number
    else:
        return first_number % 10 + sum_digits(first_number // 10)

def rectangle_area(first_number, second_number):
    return first_number ** second_number

def square_root(first_number):
    if first_number < 0:
        return "Ошибка: извлечение квадратного корня из отрицательного числа"
    return round(math.sqrt(first_number), 2)


def factorial(first_number):
    if first_number < 0:
        return "Ошибка: факториал отрицательного числа не определен"
    if first_number == 0:
        return 1
    result = 1
    for i in range(1, int(first_number) + 1):
        result *= i
    return result


def sin(first_number):
    return round(math.sin(first_number), 2)


def cos(first_number):
    return round(math.cos(first_number), 2)


def tan(first_number):
    return round(math.tan(first_number), 2)



print('_' * 5, 'Калькулятор', '_' * 5)
print('Выберите номер операции')

while True:
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Проверка на четность")
    print("12. Функцию , которая принимает положительное целое число и возвращает сумму его цифр")
    print("13. rectangle_area")
    print("0. Выход")
    s = input('Номер операции ')

    if s == '0':
        break

    if s not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11','12','13'):
        print('Неверный номер операции')
        continue

    try:
        first_number = float(input("Введите первое число: "))
        if s != '6' and s != '7' and s!='11' and s!= '12' :
            second_number = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите числа корректно")
        continue

    if s == '1':
        print("Результат:", sum_numbers(first_number, second_number))
    elif s == '2':
        print("Результат:", defference_numbers(first_number, second_number))
    elif s == '3':
        print("Результат:",multiply(first_number, second_number) )
    elif s == '4':
        if second_number != 0:
            print("Результат:", divide_numbers(first_number, second_number))
        else:
            print('Нельзя делить на ноль')
    elif s == '5':
        print("Результат:", rectangle_area(first_number, second_number))
    elif s == '6':
        if first_number >= 0:
            print("Результат:", square_root(first_number))
        else:
            print('Нельзя извлечь корень из отрицательного числа')
    elif s == '7':
        if first_number >= 0:
            print("Результат:", factorial(first_number))
        else:
            print('Факториал отрицательного числа не определен')
    elif s == '8':
        print("Результат:", sin(first_number))
    elif s == '9':
        print("Результат:", cos(first_number))
    elif s == '10':
        print("Результат:", tan(first_number))
    elif s == '11':
        print("Результат:", is_even(first_number))
    elif s == '12':
        print("Результат:", sum_digits(first_number))
    elif s == '13':
        print("Результат:", rectangle_area(first_number,second_number ))



