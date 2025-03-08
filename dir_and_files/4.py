def count_lines():
    file_path = r'C:\Users\Hp Omen\lab6\file_checker.py'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return len(lines)

print("Number of lines:", count_lines())
