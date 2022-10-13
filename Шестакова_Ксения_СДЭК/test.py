# print(*[el for el in map(str.capitalize, input().split())])
# если нужно чтобы первые буквы были заглавными, а остальные строчными

# а этот вариант если нужно, чтобы изменялись только первые буквы слова
print(*[el for el in map(lambda x: f'{x[0].upper()}{x[1:]}', input().split())])