a = []
for i in range(int(input("Введите размерность списка: "))):
    a.append(int(input(str(i + 1)+") ")))
b = list(map(lambda x: x * 2, list(filter(lambda x: x > 5 , a))))
try:
    print("Max:", max(b), "\nSum:", sum(b))
except BaseException:
    print("Введены неподходящие данные")
