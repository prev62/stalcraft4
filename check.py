import os

# Укажите путь к папке с файлами
folder_path = './cookies'

# Имя файла для вывода
output_file = 'output.txt'

# Получаем список файлов в папке
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

with open(output_file, 'w') as file:
    for i, filename in enumerate(files, start=1):
        # Формируем строку для script и run_script_in_new_window
        script_line = f'    script{i} = \'{filename}\''
        run_script_line = f'    run_script_in_new_window(script{i})'
        
        # Записываем строки в файл
        file.write(script_line + '\n')
    
    file.write('\n')  # Разделяем блоки
    for i in range(1, len(files) + 1):
        run_script_line = f'    run_script_in_new_window(script{i})'
        file.write(run_script_line + '\n')
        
print(f"Скрипт завершен. Данные сохранены в {output_file}.")
