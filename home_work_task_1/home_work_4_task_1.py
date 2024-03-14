from pathlib import Path
import re

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as document:
            document_file = document.read()
            numbers_str = re.findall(r"\d+", document_file)
            document_info = document_file.splitlines()
            document_info = [doc.strip() for doc in document_info if doc.strip()]
            numbers = []
            for num_str in numbers_str:
                numbers.append(int(num_str))
            total = sum(numbers)
            average = total // len(numbers)
            print(f"Список працівників: {document_info}")
            print(f"Заробітня плата працівників: {numbers}")
            return total, average         
            
    except:
        pass


total, average = total_salary('C:/Users/User/Desktop/home_work_4/home_work_task_1/document.txt') 
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




