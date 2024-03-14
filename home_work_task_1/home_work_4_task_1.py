from pathlib import Path
import re
import math

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as document:
            document_file = document.read()
            # pattern = r"\d+"
            numbers = re.findall(r"\d+", document_file)
            document_info = document_file.splitlines()
            document_info = [doc.strip() for doc in document_info if doc.strip()]
            print(document_info)
            print(numbers)
    except:
        pass


path = total_salary('C:/Users/User/Desktop/home_work_4/home_work_task_1/document.txt') 


