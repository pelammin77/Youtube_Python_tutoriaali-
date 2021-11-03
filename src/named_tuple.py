from collections import namedtuple

# tuple_point = (5, 3, 1)
#
# print(type(tuple_point))
# # #
# print(tuple_point)
# print(tuple_point[0])
# #
#
Point = namedtuple('Point', 'x y z')

piste = Point(5, 3, 10)

print(piste)
#
#
print(piste._fields)
print(piste.x, piste.y, piste.z)
print(piste[0], piste[1], piste[2])
#
new_dict = piste._asdict()
#
piste = piste._replace(x=7, y=2)
#
print(piste)
#
piste = piste._make([0, 5, 9])
print(piste)
