def parametrs(a, b, c):

    d = b**2 - 4*a*c  # Створюю змінну - формулу дискримінанта для знаходження коренів р-ня

    if d == 0:  # Коли дискримінант рівний 0
        k = - b / 2*a
        return k
    elif d > 0:  # Коли дискримінант більше за 0
        k1 = (-b + d ** 1 / 2) / 2 * a  # Корінь 1
        k2 = (-b - d ** 1 / 2) / 2 * a  # Корінь 2
        print('Корені р-ня дорвінюють:')
        return k1, k2
    else:  # Коли дискримінант менше за 0
        print('Дискримінант від`ємний, отже:')
        return 'коренів не знайдено'

a = int(input('Введіть коефіцієнт a:'))
b = int(input('Введіть коефіцієнт b:'))
c = int(input('Введіть коефіцієнт c:'))

result = parametrs(a, b, c)
print(result)