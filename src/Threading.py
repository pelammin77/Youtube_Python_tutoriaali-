
import concurrent.futures
import time

aloitus_aika = time.time()


def tee_jutut(viive):

    print("Torku", viive,"sekutti")
    time.sleep(viive)
    return "Torkut ohi"

#viive = 2


with concurrent.futures.ThreadPoolExecutor() as executor:
    res_list =[executor.submit(tee_jutut, 1)for _ in range(10)]

    for f in concurrent.futures.as_completed(res_list):
        print(f.result())








    # f1 = executor.submit(tee_jutut, 2)
    # f2 = executor.submit(tee_jutut, 2)
    # print(f1.result())
    # print(f2.result())



lopetus_aika = time.time()

print(f'Suorittaminen kesti {round(lopetus_aika - aloitus_aika,2)} sekunttia')
#


#
#
#
# import threading
# from queue import Queue
# import time
#
# print_lock = threading.Lock()
# q = Queue()
#
#
# def tehtava(worker):
#     time.sleep(2) # pretend to do some work.
#     with print_lock:
#         print(threading.current_thread().name,worker)
#
# def hoida_homma():
#         while True:
#             tekija = q.get()
#             tehtava(tekija)
#             q.task_done()
#
#
# for x in range(10):
#     t = threading.Thread(target=hoida_homma)
#
#     t.daemon = True
#     t.start()
#
# start = time.time()
#
#
# for task in range(20):
#      q.put(task)
#
# q.join()
#
#
# print('Homma vei aikaa :', time.time() - start)
#
#



#
# import time
# import threading
#
# thred_list = []
#
# aloitus_aika = time.time()
#
#
# def tee_jutut():
#     print("Homma alkaa")
#     print("Torku", viive,"sekutti")
#     time.sleep(viive)
#     print("Torkut ohi")
#
# viive = 2
#
# for _ in range(10):
#     t = threading.Thread(target=tee_jutut)
#     t.start()
#     thred_list.append(t)
#
#
# for thred in thred_list:
#     thred.join()
#
#
#
# lopetus_aika = time.time()
#
# print(f'Suorittaminen kesti {round(lopetus_aika - aloitus_aika,2)} sekunttia')

#
#














#
# import time
# import threading
#
#
#
# aloitus_aika = time.time()
#
#
# def tee_jutut(viive):
#     print("Homma alkaa")
#     print("Torku", viive,"sekutti")
#     time.sleep(viive)
#     print("Torkut ohi")
#
# viive = 2
#
# # tee_jutut()
# # tee_jutut()
#
# t1 = threading.Thread(target=tee_jutut, args=[1] )
# t2 = threading.Thread(target=tee_jutut, args=[1])
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# lopetus_aika = time.time()
#
# print(f'Suorittaminen kesti {round(lopetus_aika - aloitus_aika,2)} sekunttia')
#

