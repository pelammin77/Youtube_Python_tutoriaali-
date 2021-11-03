from collections import deque

alkuluvut = (3,5, 7)

deck = deque(maxlen=3)
prime = deque(alkuluvut)

#
# prime.append(11)
# prime.append(13)
# print(prime)
# prime.appendleft(2)
# prime.appendleft(1)
# print(prime)
# luku = prime.pop()
# print(luku)
# print(prime)
#
# left_luku = prime.popleft()
# #
# #
#
# print(left_luku)
# print(prime)
#


#deck.append('Pete')
# deck.extend('Pete')
#
# print(deck)
# #
# print(deck.count('e'))
# #
# uusi_deck = deck.copy()
# print(uusi_deck)
# #
# deck.rotate(-1)
# print(deck)

deck.appendleft(1)
deck.appendleft(2)
deck.appendleft(3)
print(deck)
#
deck.appendleft(4)
print(deck)
#
