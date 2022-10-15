# print(*[el for el in map(str.capitalize, input().split())])
# если нужно чтобы первые буквы были заглавными, а остальные строчными, через один пробел каждое слово

# этот вариант если нужно, чтобы изменялись только первые буквы слова
# print(*[el for el in map(lambda x: f'{x[0].upper()}{x[1:]}', input().split())])
# но эта версия уберёт все лишние пробелы (ввод: "hhh   hh", вывод: "Hhh Hh", а ожидалось, наверное, "Hhh   Hh"

# а эта версия оставит прежнее количество пробелов
sp = []
for el in input().split(' '):
    if el:
        sp.append(f'{el[0].upper()}{el[1:]}')
    else:
        sp.append(el)
print(*sp)