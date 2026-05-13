

import os
from PIL import Image

# Папка с PNG — текущая директория
input_folder = '.'
# Папка для JPG — можно оставить ту же или указать другую
output_folder = '.'   # если хотите положить JPG рядом с PNG
# output_folder = './jpg_output'   # если хотите в отдельную папку

# Создать output_folder, если нужно
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Перебираем все файлы и папки
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.lower().endswith(".png"):
            full_path = os.path.join(root, filename)
            # Открываем PNG
            img = Image.open(full_path)
            # Конвертируем RGBA → RGB (JPG не поддерживает прозрачность)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            # Формируем новое имя (меняем расширение)
            name_without_ext = os.path.splitext(filename)[0]
            # Сохраняем в output_folder, сохраняя структуру подпапок (если нужно)
            rel_path = os.path.relpath(root, input_folder)
            out_dir = os.path.join(output_folder, rel_path)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            out_file = os.path.join(out_dir, name_without_ext + ".jpg")
            img.save(out_file, "JPEG", quality=90)
            print(f"Конвертирован: {full_path} -> {out_file}")

print("Готово!")

