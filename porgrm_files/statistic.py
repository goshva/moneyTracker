import os
import hashlib

def find_duplicate_files(path):
    """
    Находит дубликаты файлов в указанной директории.

    Args:
        directory (str): Директория, в которой нужно найти дубликаты файлов.

    Returns:
        list: Список кортежей (имя_файла, путь_к_файлу).
    """

    # Словарь для хранения хэшей файлов и их путей
    file_hashes = {}

    # Список дубликатов файлов
    duplicates = []

    # Перебор всех файлов в директории
    for root, dirs, files in os.walk(path):
        for file in files:
            # Получение пути к файлу
            file_path = os.path.join(root, file)

            # Вычисление хэша файла
            with open(file_path, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()

            # Проверка наличия хэша в словаре
            if file_hash in file_hashes:
                # Если хэш уже есть, значит файл является дубликатом
                duplicates.append((file, file_path))
            else:
                # Если хэша нет, добавляем его в словарь
                file_hashes[file_hash] = file_path

    return duplicates


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
duplicates = find_duplicate_files(path)

# Печать списка дубликатов файлов
for file, path in duplicates:
    print(f"Дубликат: {file} ({path})")


'''
import os
import hashlib

def find_duplicate_files(directory):
    """
    Находит дубликаты файлов в указанной директории.

    Args:
        directory (str): Директория, в которой нужно найти дубликаты файлов.

    Returns:
        list: Список кортежей (имя_файла, путь_к_файлу).
    """

    # Словарь для хранения хэшей файлов и их путей
    file_hashes = {}

    # Список дубликатов файлов
    duplicates = []

    # Перебор всех файлов в директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Получение пути к файлу
            file_path = os.path.join(root, file)

            # Вычисление хэша файла
            with open(file_path, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()

            # Проверка наличия хэша в словаре
            if file_hash in file_hashes:
                # Если хэш уже есть, значит файл является дубликатом
                duplicates.append((file, file_path))
            else:
                # Если хэша нет, добавляем его в словарь
                file_hashes[file_hash] = file_path

    return duplicates


# Пример использования
directory = "/path/to/directory"
duplicates = find_duplicate_files(directory)

# Печать списка дубликатов файлов
for file, path in duplicates:
    print(f"Дубликат: {file} ({path})")

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
