
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
      print('Found It!')
      continue
    print(num)

print('\t')

for num in nums:
    for letter in 'abc':
        print(num, letter)

print('\t')

for i in range(1, 11):
    print(i)

print('\t')

x=0

while x < 10:
    print(x)
    x += 1

#Infinite Loop

x=0

while True:
    print(x)
    x += 1
