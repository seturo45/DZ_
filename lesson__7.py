# задание 1
import os
my_script = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in my_script.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            my_dir = os.path.join(root, folder)
            os.makedirs(my_dir)


# задание 3
import shutil

my_dir_3 = 'task_3'
if not os.path.exists(my_dir_3):
    os.mkdir(my_dir_3)

folder = r'my_project'
files = []

for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder = os.path.join(my_dir_3, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)



# задание 4
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
        out_dict[10 ** len(str(file))] += 1
print(out_dict)