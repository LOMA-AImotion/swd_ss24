def my_double_list(l : list) -> list:
    def my_double(x : int) -> int:
        return 2*x
    return [my_double(i) for i in l]

print(my_double_list([2,4,6]))
print(my_double(12))