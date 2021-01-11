
import datetime
import my_module
'''import sys'''

Writers = ['John Green', 'JK Rowling', 'Stephen King', 'Dan Brown']

index = my_module.find_index(Writers, 'John Green')
print(index)

# print(sys.path)

import random

random_writer = random.choice(Writers)

print(random_writer)

today = datetime.date.today()
print('\t')
print(today)

