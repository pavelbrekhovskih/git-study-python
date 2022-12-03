print('Факториал')
def sum_factorials(num):
    part_factorial = 1
    summa = 0

    for i in range(1, num + 1):
        part_factorial *= i
        summa += part_factorial
    return summa


n = int(input("Введите число: "))
print(sum_factorials(n))

print("Задача 2. НОД")
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print('Наибольший общий делитель:', a + b)

gcd (4782 , 698)
print()