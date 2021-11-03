
import time
import multiprocessing
import math
import os


def laske_jutut():
    for i in range(0, 10000):
        math.sqrt(i)
#
#
# def main():
#     process_list = []
#     aloitus_aika = time.time()
#     for i in range(os.cpu_count()):
#         print("Luodaan processi", i+1)
#         process_list.append(multiprocessing.Process(target=laske_jutut))
#     for p in process_list:
#         p.start()
#     for process in process_list:
#         process.join()
#     lopetus_aika = time.time()
#     print(f'Suorittaminen kesti {round(lopetus_aika - aloitus_aika,2)} sekunttia')
#
#
# if __name__ == '__main__':
#
#     print("Alkaa")
#     main()
#
#

process_list = []
aloitus_aika = time.time()
for i in range(os.cpu_count()):
    print("Luodaan processi", i+1)
    process_list.append(multiprocessing.Process(target=laske_jutut))
for p in process_list:
    p.start()
for process in process_list:
    process.join()
lopetus_aika = time.time()
print(f'Suorittaminen kesti {round(lopetus_aika - aloitus_aika,2)} sekunttia')
