import os

def rename_files(source_dir, target_dir):
    # Получаем список файлов из папки с новыми именами
    source_files = sorted(os.listdir(source_dir))
    
    # Получаем список файлов из папки для переименования
    target_files = sorted(os.listdir(target_dir))
    
    # Проверяем, что количество файлов совпадает
    if len(source_files) != len(target_files):
        print("Количество файлов в папках не совпадает.")
        return
    
    # Переименовываем файлы
    for source_file, target_file in zip(source_files, target_files):
        source_path = os.path.join(source_dir, source_file)
        target_path = os.path.join(target_dir, target_file)
        # Генерируем новое имя с расширением .py
        new_file_name = os.path.splitext(source_file)[0] + '.py'
        new_target_path = os.path.join(target_dir, new_file_name)

        # Проверяем, существует ли файл с новым именем
        if os.path.exists(new_target_path):
            print(f'Файл с именем {new_file_name} уже существует в папке {target_dir}. Пропуск.')
            continue
        
        # Переименовываем файл в целевой папке
        os.rename(target_path, new_target_path)
        print(f'Файл {target_file} переименован в {new_file_name}')

# Пример использования
source_directory = 'cookies'  # Папка с новыми именами файлов
target_directory = 'names'    # Папка, где нужно переименовать файлы

rename_files(source_directory, target_directory)
