import os
from PIL import Image
import easyocr
import numpy as np

def is_text_upside_down_easyocr(image_path, lang='ru+en'):
    """
    Определяет, перевёрнут ли текст на изображении с помощью EasyOCR.
    Возвращает True, если текст перевёрнут (требуется поворот на 180°).
    """
    try:
        # Инициализируем EasyOCR (первый запуск может загрузить модели)
        reader = easyocr.Reader(['ru', 'en'])  # Русский и английский
        
        # Открываем изображение и конвертируем в numpy array
        img = Image.open(image_path)
        img_np = np.array(img)
        
        # Детектируем текст и его ориентацию
        results = reader.readtext(img_np, rotation_info=[0, 90, 180, 270])
        
        # Если EasyOCR нашёл текст только при повороте на 180°, значит он перевёрнут
        for (bbox, text, prob), angle in [(r[:3], r[2]) for r in results]:
            if angle == 180 and prob > 0.6:  # Порог уверенности 60%
                return True
        return False
        
    except Exception as e:
        print(f"Ошибка EasyOCR для {image_path}: {str(e)}")
        return False

def rotate_images_with_upside_down_text(folder_path):
    """Переворачивает на 180° только изображения с перевёрнутым текстом"""
    if not os.path.exists(folder_path):
        print(f"Папка {folder_path} не существует!")
        return

    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp')
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_formats):
            file_path = os.path.join(folder_path, filename)
            
            if is_text_upside_down_easyocr(file_path):
                try:
                    with Image.open(file_path) as img:
                        rotated_img = img.rotate(180)
                        rotated_img.save(file_path)
                        print(f"Повёрнуто: {filename}")
                except Exception as e:
                    print(f"Ошибка при повороте {filename}: {str(e)}")
            else:
                print(f"Пропущено (текст в норме): {filename}")

if __name__ == "__main__":
    photos_folder = "photos"  # Укажите вашу папку
    rotate_images_with_upside_down_text(photos_folder)