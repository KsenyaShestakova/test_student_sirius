## Обо мне (чуть-чуть)

Мне нравится программирование, мне бы хотелось развиваться в этой 
сфере, поэтому я обучалась python на курсах Яндекс.Лицея 2 года. Во время 
обучения мы разрабатывали собственные небольшие проекты, это давало 
нам попрактиковаться в разработке программ/приложений, также в качестве 
командного проекта мы создавали web-приложение.

e-mail: ksenya.shestakova.07@yandex.ru

my [github profile](https://github.com/KsenyaShestakova): https://github.com/KsenyaShestakova 

## Task 3.1
My code:
```python
# эта версия оставит прежнее количество пробелов
sp = []
for el in input().split(' '):
    if el:
        sp.append(f'{el[0].upper()}{el[1:]}')
    else:
        sp.append(el)
print(*sp)
```

Tests:

| ввод                      | вывод                     |
|---------------------------|---------------------------|
| hbdth HGFHjhjhg JHGF hsfg | Hbdth HGFHjhjhg JHGF Hsfg |
| Привет, мир!              | Привет, Мир!              |
| meow!! МЯУ мяу!           | Meow!! МЯУ Мяу!           |
| hhh hhh hh    k k kk      | Hhh Hhh Hh    K K Kk      |