# задание 1
# with open('nginx_logs.txt') as file_1:
#     data = []
#     for line in file_1:
#         splitted = line.split()
#         data.append((splitted[0], splitted[5].replace('"', ''), splitted[6], splitted[7]))
# print(data)


# задание 3

import json
from itertools import zip_longest
names = ['Иванов,Иван,Иванович\n',
         'Петров,Петр,Петрович\n'
         'Сидоров,Михаил,Сергеевич']
hobbies = ['скалолазание,охота\n',
           'горные лыжи']
out_dict = {}
with open('users.csv', 'w+', encoding='utf-8') as users:
    users.writelines(names)
    with open('hobby.csv', 'w+', encoding='utf-8') as hobby:
        hobby.writelines(hobbies)
        num_lines_users = sum(1 for line in users)
        num_lines_hobby = sum(1 for lines in hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(users, hobby):
            out_dict[line_user.strip()] = line_user_hobby.strip() if \
                line_user_hobby is not None else line_user_hobby

with open('task_3.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f)
print(out_dict)


# задание 4

with open('task_4.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', 'w+', encoding='utf-8') as users:
        users.writelines(names)
        with open('hobby.csv', 'w+', encoding='utf-8') as hobby:
            hobby.writelines(hobbies)
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for lines in hobby)

            if num_lines_users < num_lines_hobby:
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobby):
                f.write(f'{line_user.strip()}: '
                        f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')

