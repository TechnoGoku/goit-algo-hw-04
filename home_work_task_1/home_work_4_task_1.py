from pathlib import Path

def total_salary(path):
    with open(path, 'r', encoding='utf-8') as document:
        document_file = document.read()
        document_info = document_file.split(',')
        document_info = []
        print(document_info)



path = total_salary('C:/Users/User/Desktop/home_work_4/home_work_task_1/document.txt') 