
def hello_func():
    print('Hello Function!')

hello_func()
hello_func()
print('\t')
print('Hello Function!')
print('Hello Function!')

def hello_function(greeting, name='You'):
    return '{}, {}'.format(greeting, name)
print('\n')
print(hello_function('Hi', name = 'Faizul Islam'))


def student_info(*Banana, **Monkey):
    print(Banana)
    print(Monkey)

student_info('ECE', 'Department', name='Faizul', surname='Islam')

