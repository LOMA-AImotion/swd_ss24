def my_func(zahl : int) -> int:
    return 2 * zahl

print(my_func(10))
func_ref = my_func
print(func_ref(20))

from functools import partial
no_arg_ref = partial(my_func, 15)
print(no_arg_ref())