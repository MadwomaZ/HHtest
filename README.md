# Тестовые задачи для поступления в школу программистов HeadHunter

#####Полином

Дано выражение, содержащее скобки, операции сложения, вычитания, умножения, возведения в константную степень и одну переменную, например: (x - 5)(2x^3 + x(x^2 - 9)).

Представьте это выражение в развёрнутом виде, например: 3x^4 - 15x^3 - 9x^2 + 45x

#####Бесконечная последовательность

Возьмём бесконечную цифровую последовательность, образованную склеиванием последовательных положительных чисел: S = 123456789101112131415...
Определите первое вхождение заданной последовательности A в бесконечной последовательности S (нумерация начинается с 1).

Пример входных данных:
6789
111

Пример выходных данных:
6
12

Сравнивая символы бесконечной последовательности и входные данные, находим первое вхождение последовательности(входные данные) и возвращаем его индекс.

######Как использовать:
python hh2.py NUM, где NUM - число для которого требуется найти индекс
