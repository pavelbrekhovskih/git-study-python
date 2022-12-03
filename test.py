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

print('Задача 6. Спецшифр_1')      #Задачи на максимум решать со сравнения с 0
text = input('Введите строку: ') #ssbbbsssbc sssbbbssbc  sbbbssssbbbbs sssbcbcbcbc aaassaabbs
s_count = 0 # текущее количество s
s_count_max = 0 # максимальное количество s

for symb in text:
    if symb == 's':
        s_count += 1
    else:
        s_count = 0
    if s_count > s_count_max:
        s_count_max = s_count

print('Самая длинная последовательность: ', s_count_max)
print("-----------------------------------------------------------------------------------")