from vector import Vector

#VALID TESTS
integer = 4
float_list = [1.0, 2.0, 3.0]
int_range = (10, 13)
try:
	v1 = Vector(integer)
	v2 = Vector(float_list)
	v3 = Vector(int_range)
	print(str(v1), end = '')
	print(str(v2), end = '')
	print(str(v3), end = '')
except:
	pass

#INVALID TESTS
integer = "3"
float_list = [0.0, 1.0, "2.0"]
int_range = ("10", 15)
try:
	fv1 = Vector(integer)
	fv2 = Vector(float_list)
	fv3 = Vector(int_range)
	int_range = (10, 15, 20)
	fv4 = Vector(int_range)
except:
	pass

#VALID OPERATIONS
v4 = v2 + v3
v7 = v2 + 100
print(str(v4), end = '')
print(str(v7), end = '')

v5 = v2 - v3
v8 = v2 - 100
print(str(v5), end = '')
print(str(v8), end = '')

v6 = v2 * 2
print(str(v6), end = '')
dot_product = v2 * v3
print("Dot product = %f" %dot_product)

v9 = v3 / 2
print(str(v9), end = '')

#INVALID TESTS
print()
fv4 = v1 + "a"
fv5 = v1 + v3
fv6 = v1 - "b"
fv7 = v1 - v3
fv8 = v1 * "a"
fv9 = v1 / "a"
fv10 = v3 / v2
