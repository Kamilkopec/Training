# what will the following script output/

c = 1


def foo():
    c = 2
    return c


c = 3
print(foo())
# c inside a function is local to a function which is a different c than c outsite