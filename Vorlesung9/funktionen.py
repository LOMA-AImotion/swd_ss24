def my_func(x: int ) -> int:
    return 2*x

a = my_func
b = my_func(5)
c = a(10)

print(a, type(a))
print(b, type(b))
print(c, type(c))