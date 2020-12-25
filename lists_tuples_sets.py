# Lists

Courses = ['Physics', 'Geography', 'Chemistry', 'Computer Science']

print(len(Courses))

Courses.insert(2, 'Art')

print(Courses)

Courses.reverse()

print(Courses)

nums = [1, 5, 4, 3, 2]

nums.sort()

print(nums)

for index, Courses in enumerate(Courses):
    print(index, Courses)

course = ['History', 'Geography', 'Civics', 'Sociology', 'Arduino']

course_str = ' - '.join(course)

print(course_str)


# Mutable
# list_1 = ['History', 'Chemistry', 'Physics', 'CompSci']
# list_2 = list_1
#
# print(list_1)
# print(list_2)
#
# list_1[0] = 'Art'
#
# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Chemistry', 'Physics', 'CompSci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)


# Sets
cs_courses = {'History', 'Chemistry', 'Physics', 'CompSci'}
art_courses = {'Physics', 'Chemistry'}

print(cs_courses.intersection(art_courses))


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dictionary
empty_set = set()