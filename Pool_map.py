import multiprocessing
import time

# Функция для вычисления квадрата числа
def calc_square(n):
    result = n * n
    print(f'\n{n} ^ 2 = {result}')
    time.sleep(0.1)  # Имитация задержки
    return result

# Функция для вычисления куба числа
def calc_cube(n):
    result = n * n * n
    print(f'\n{n} ^ 3 = {result}')
    time.sleep(0.1)  # Имитация задержки
    return result

if __name__ == "__main__":
    numbers = [2, 3, 5, 8]  # Уменьшил диапазон для наглядности
    start = time.time()

    # Создаем пул процессов
    with multiprocessing.Pool(processes=3) as pool:
        # Применяем функции к каждому элементу списка numbers
        pool.map(calc_square, numbers)
        pool.map(calc_cube, numbers)

    end = time.time()
    print(f'Execution Time: {end - start}')