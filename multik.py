import multiprocessing
import time

def calc_square(numbers):
    for n in numbers:
        print(f'\n{n} ^ 2 = {n * n}')
        time.sleep(0.1)  # Имитация задержки

def calc_cube(numbers):
    for n in numbers:
        print(f'\n{n} ^ 3 = {n * n * n}')
        time.sleep(0.1)  # Имитация задержки

if __name__ == "__main__":
    numbers = [2, 3, 5, 8]
    start = time.time()

    # Создание процессов
    square_process = multiprocessing.Process(target=calc_square, args=(numbers,))
    cube_process = multiprocessing.Process(target=calc_cube, args=(numbers,))

    # Запуск процессов
    square_process.start()
    cube_process.start()

    # Ожидание завершения процессов
    square_process.join()
    cube_process.join()

    end = time.time()
    print(f'Execution Time: {end - start}')