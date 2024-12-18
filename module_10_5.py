import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    try:
        with open(name, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line)
    except FileNotFoundError:
        print(f"Файл {name} не найден.")

filenames = [f'D:/Project/pythonProject/files/file_{number}.txt' for number in range(1, 5)]

def linear_read():
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f'Линейное выполнение: {end_time - start_time:.6f} секунд')

def multiprocess_read():
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'Многопроцессное выполнение: {end_time - start_time:.6f} секунд')

if __name__ == '__main__':
    print("Запуск линейного выполнения:")
    linear_read()

    print("\nЗапуск многопроцессного выполнения:")
    multiprocess_read()
