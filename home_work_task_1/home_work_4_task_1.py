from pathlib import Path

def total_salary(path):
    path = Path('User/Desktop/home_work_4/home_work_task_1/document.txt')
    with open(path, 'r', encoding='utf-8') as document:
        read_file = document.read()
        print(read_file)



total_salary('C:/Users/User/Desktop/home_work_4/home_work_task_1/document.txt') 