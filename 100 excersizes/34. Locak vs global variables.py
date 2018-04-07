# the following throws a NameError in the last line saying that c is not defined.
# please fix the function so that there is no error and the last line is able
# to print out the value of c


def foo():
    global c
    c = 1
    return c


foo()
print(c)

# before adding the global keyword c was a variable local to a function
# after adding the global c become available outside the function


