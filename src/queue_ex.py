#
#
# from queue import Queue
#
# q = Queue()
# #FIFO
#
#
# print(q.qsize())
#
# # Adding of element to queue
#
# print("Onko tyhja: ", q.empty())
#
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
#
#
#
#
# print(q.qsize())
# print("Onko täynnä", q.full())
# print("Onko tyhja: ", q.empty())
#
#
# # Poisto
# print(q.get())
# print(q.get())
# print(q.get())
#
#
#
# print("Onko tyhja: ", q.empty())
#
# q.put(1)
# print(q.qsize())
# print("Tyhjä: ", q.empty())
# print("Täynnä: ", q.full())



from queue import LifoQueue
#


stack = LifoQueue(maxsize=3)

# qsize() give the maxsize
# of the Queue
print(stack.qsize())

# Adding of element to queue
stack.put(1)
stack.put(2)
stack.put(3)


print(stack.qsize())
print("Onko täynnä", stack.full())


# Poisto
print(stack.get())
print(stack.get())
print(stack.get())



print("Onko tyhja: ", stack.empty())

stack.put(1)
print("Tyhjä: ", stack.empty())
print("Täynnä: ", stack.full())
