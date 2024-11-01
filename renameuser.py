import os

def update_username_field(file_path, new_username):
    """Обновляет поле username в файле."""
    # Читаем содержимое файла
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Обновляем строку с полем username
    updated_lines = []
    for line in lines:
        if line.strip().startswith('username='):
            updated_lines.append(f'    username="{new_username}",\n')
        else:
            updated_lines.append(line)
    
    # Записываем обновленное содержимое обратно в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)
    
    print(f'В файле {file_path} обновлено поле username на: {new_username}')

def update_all_files_in_directory(directory):
    """Обновляет поле username во всех файлах в указанной папке."""
    # Получаем список файлов из папки
    files = sorted(os.listdir(directory))
    
    # Обновляем поле username в каждом файле
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        
        # Проверяем, является ли объект файлом
        if os.path.isfile(file_path):
            # Получаем имя файла без расширения
            new_username = os.path.splitext(file_name)[0]
            
            # Обновляем поле username в файле
            update_username_field(file_path, new_username)

# Пример использования
target_directory = 'names'    # Папка, где нужно обновить файлы

update_all_files_in_directory(target_directory)