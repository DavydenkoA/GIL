import multiprocessing
import time

# Функция для выполнения всех вычислений
def calc_all(n):
    square = n * n
    cube = n * n * n
    print(f'\n{n} ^ 2 = {square}, {n} ^ 3 = {cube}')
    time.sleep(0.1)  # Имитация задержки
    return square, cube

if __name__ == "__main__":
    numbers = [2, 3, 5, 8]  # Уменьшил диапазон для наглядности
    start = time.time()

    # Создаем пул процессов
    with multiprocessing.Pool() as pool:
        # Применяем функцию calc_all к каждому элементу списка numbers
        pool.map(calc_all, numbers)

    end = time.time()
    print(f'Execution Time: {end - start}')