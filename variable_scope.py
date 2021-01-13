'''
LEGB
Local, Enclosing, Global, Built-in
'''

# x = 'global x'
#
# def test():
#     x = 'local x'
#     #print(y)
#     print(x)
#
# test()
# print(x)

import builtins

# print(dir(builtins))

# def my_min():
#     # pass
#
# m = min([5, 1, 4, 2, 3])
# print(m)
#
#
#
# def test(z):
#     x = 'local x'
#     print(z)
#
# test('local z')

x = 'global x'

def outer():

    def inner():
        print(x)

    inner()
    print(x)

outer()
print(x)

