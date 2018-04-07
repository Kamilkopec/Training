# why is there an error in the code and how would ypou fix it?


def foo(a=1, b=2):
    return a + b


x = foo - 1
# wrong method call
# he will return Type error
# type(foo) =  function which is an object
# type(foo() = int which is the function call

print(x)
