import os
import re

# Путь к вашему файлу
file_path = 'main.py'

# Путь к папке с файлами скриптов
scripts_folder = 'names'

# Получаем список файлов из папки 'names' и сортируем их для последовательной замены
script_files = sorted([f for f in os.listdir(scripts_folder) if f.endswith('.py')])

# Считываем содержимое файла
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Шаблон для поиска строк вида scriptX = 'filename.py'
pattern = r'(script\d+\s*=\s*[\'"])[^\'"]+([\'"])'

# Функция замены, которая берет следующий файл из списка script_files
def replace_filename(match):
    global script_files
    if script_files:
        # Заменяем содержимое кавычек на следующий файл из списка
        return f"{match.group(1)}{script_files.pop(0)}{match.group(2)}"
    else:
        return match.group(0)  # Возвращаем исходное значение, если файлов не хватает

# Выполняем замену
content = re.sub(pattern, replace_filename, content)

# Записываем изменения обратно в файл
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print("Имена файлов заменены!")
