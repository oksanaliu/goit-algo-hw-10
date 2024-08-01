# Обчислення визначеного інтеграла методом Монте-Карло

## Опис
Цей проект включає обчислення значення інтеграла функції \( f(x) = x^2 \) на інтервалі [0, 2] методом Монте-Карло та порівняння результату з аналітичним значенням, отриманим за допомогою функції quad з бібліотеки SciPy.

## Результати
- Значення інтеграла методом Монте-Карло: 2.6591562226602012
- Значення інтеграла за допомогою функції `quad`: 2.6666666666666665
- Абсолютна помилка: 2.9605947323337504e-14

## Висновки
- Метод Монте-Карло показав високу точність для обчислення значення інтеграла функції \( f(x) = x^2 \) на заданому інтервалі. Результати, отримані за допомогою методу Монте-Карло, добре узгоджуються з результатами, отриманими за допомогою функції quad з бібліотеки SciPy, що підтверджує ефективність та надійність методу Монте-Карло для даного типу задач.
- Абсолютна помилка між результатами методів є дуже малою, що свідчить про високу точність методу Монте-Карло.

Цей проект дозволяє зрозуміти, як використовувати метод Монте-Карло для обчислення визначених інтегралів і порівняти отримані результати з точними аналітичними розрахунками.