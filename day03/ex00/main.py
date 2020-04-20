from NumPyCreator import NumPyCreator

npc = NumPyCreator()
my_array = npc.from_list([[1, 4, 2, 5, 7], [8, 0, 1, 9, 2]])
print(type(my_array))
print(my_array)

my_array = npc.from_tuple((2, 3))
print(type(my_array))
print(my_array)

my_array = npc.from_iterable(range(510))
print(type(my_array))
print(my_array)

shape = (2, 6)
my_array = npc.from_shape(shape, int)
print(type(my_array))
print(my_array)

my_array = npc.random(shape)
print(type(my_array))
print(my_array)

my_array = npc.identity(4)
print(type(my_array))
print(my_array)
