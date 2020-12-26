# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')


user = 'Admin'
signed_in = True

if user == 'Admin' and signed_in:
    print('Admin Page')
else:
    print('Invalid Format')