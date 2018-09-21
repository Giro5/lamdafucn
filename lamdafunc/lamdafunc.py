a = list(map(lambda x: int(x), input("Введите элементы списка через пробел\n").split(" ")))
b = list(map(lambda x: x * 2, list(filter(lambda x: x > 5 , a))))
try:
    print("Max:", max(b), "\nSum:", sum(b))
except BaseException:
    print("Введены неподходящие данные")
