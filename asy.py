import asyncio
import time

async def calc_square(numbers):
    for n in numbers:
        print(f'\n{n} ^ 2 = {n * n}')
        await asyncio.sleep(0.1)  # Имитация асинхронного ожидания

async def calc_cube(numbers):
    for n in numbers:
        print(f'\n{n} ^ 3/2 = {n * n * n}')
        await asyncio.sleep(0.1)  # Имитация асинхронного ожидания

async def main():
    numbers = [2, 3, 5, 8]
    start = time.time()

    # Запуск асинхронных задач
    square_task = asyncio.create_task(calc_square(numbers))
    cube_task = asyncio.create_task(calc_cube(numbers))

    # Ожидание завершения обеих задач
    await square_task
    await cube_task

    end = time.time()
    print(f'Execution Time: {end - start}')

# Запуск асинхронной программы
if __name__ == "__main__":
    asyncio.run(main())