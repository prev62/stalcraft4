import os

def run_script_in_new_window(script_name):
    # Реализуйте здесь код, который будет запускать скрипт в новом окне
    # Например, используйте команду для открытия нового окна в зависимости от операционной системы
    print(f'Запуск скрипта: {script_name}')  # Замените это на реальную логику запуска

# Путь к папке, которую нужно сканировать
folder_path = 'names'

# Получаем список всех файлов в папке
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Создаем список с именами скриптов
scripts = []

for i, file_name in enumerate(files, start=1):
    script_name = f"script{i} = '{file_name}'"
    scripts.append(file_name)  # Сохраняем имена файлов в список
    # Печатаем строку с названием переменной (не обязательно)
    print(script_name)

# Выполняем вызовы функции после создания всех переменных
for script_file in scripts:
    run_script_in_new_window(script_file)