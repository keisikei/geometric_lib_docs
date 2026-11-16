# Unit тесты к geometric_lib

Geometric_lib - Библиотека вычисления площади и периметра фигур
Тут реализованы unit тесты к ней

## Состав

| Файл | Что внутри |
|---|---|
| rectangle.py | площадь и периметр прямоугольника |
| triangle.py | площадь и периметр треугольника |
| circle.py | площадь и длина окружности |
| square.py | площадь и периметр квадрата |
| test_rectangle.py | 12 unit-тестов |
| test_triangle.py | 10 unit-тестов |
| test_circle.py | 8 unit-тестов |
| test_square.py | 8 unit-тестов |
| docs/testing_plan.md | план тестирования и ручные тест-кейсы |

## Запуск всех тестов разом

    python -m unittest discover -v

## Запуск тестов только конкретного одного модуля

    python -m unittest test_rectangle.py -v

! - На macOS вместо `python` используется `python3`.

## Результат

**Ran 32 tests — OK**