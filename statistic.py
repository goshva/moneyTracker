import os

def count_files_with_prefix(path, prefix):
    count = 0
    count2 = 0
    for filename in os.listdir(path):
        if filename.endswith('.jpg'):
            if filename.startswith(prefix):
                count += 1
            else:
                count2 += 1
    return count, count2

path = "."  # Укажите путь к папке
prefix = 'photo_'
count, count2 = count_files_with_prefix(path, prefix)
print(f"файлы требующие переименования '{prefix}': {count}")
print(f"файлы не требующие переименования '{prefix}': {count2}")



'''
import os

folder_path = '/путь/к/папке'
count = 0

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        count += 1

print(f'Количество картинок: {count}')





как работают __
file_count = sum(len(files) for _, _, files in os.walk(path))
print("Количество файлов в папке:", file_count)
'''