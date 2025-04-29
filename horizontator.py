import os
from PIL import Image

def rotate_vertical_images_in_folder(folder_path):
    # Проверяем, существует ли папка
    if not os.path.exists(folder_path):
        print(f"Папка {folder_path} не существует!")
        return
    
    # Получаем список файлов в папке
    files = os.listdir(folder_path)
    
    # Поддерживаемые форматы изображений
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    
    for file in files:
        # Проверяем расширение файла
        if file.lower().endswith(supported_formats):
            try:
                # Формируем полный путь к файлу
                file_path = os.path.join(folder_path, file)
                
                # Открываем изображение
                with Image.open(file_path) as img:
                    width, height = img.size
                    
                    # Проверяем, вертикальное ли изображение (высота > ширины)
                    if height > width:
                        # Поворачиваем на 90 градусов по часовой стрелке
                        rotated_img = img.rotate(-90, expand=True)
                        
                        # Сохраняем изображение (перезаписываем оригинал)
                        rotated_img.save(file_path)
                        print(f"Вертикальное изображение {file} повернуто.")
                    else:
                        print(f"Горизонтальное изображение {file} пропущено.")
                    
            except Exception as e:
                print(f"Ошибка при обработке изображения {file}: {e}")

if __name__ == "__main__":
    # Укажите путь к папке с фотографиями
    photos_folder = "photos"
    rotate_vertical_images_in_folder(photos_folder)