
print("Программа проверки равенства трех чисел")
print("Введите числа")
first = int(input("число 1: "))
second = int(input("число 2: "))
third = int(input("число 3: "))
print("РЕЗУЛЬТАТ:")

if first == second and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)