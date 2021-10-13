# Задание 1
n = int(input('Enter N: '))

def my_gen_1(n):
    for num in range(1, n + 1, 2):
        yield num

print(*my_gen_1(n))
# print(type(my_gen_1(n)))


# Задание 2
my_gen_2 = (num for num in range(1, n+1, 2))
print(*my_gen_2)
# print(type(my_gen_2))


# Задание 3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
my_gen_3 = ((tutors, classes) for tutors, classes in zip(tutors, classes))
print(*my_gen_3)
print(type(my_gen_3))


# Задание 4
src_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num for i, num in enumerate(src_1) if num > src_1[i - 1] and i != 0]
print(result)


# Задание 5
src_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [i for i in src_2 if src_2.count(i) == 1]
print(result)
