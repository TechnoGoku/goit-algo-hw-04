from pathlib import Path
import re

def total_salary(path):
    path = Path(__file__).parent / path
    print(path)
    try:
        with open(path, 'r', encoding='utf-8') as document:
            document_file = document.read()
            document_info = document_file.splitlines()
            for doc in document_info:
                if doc.strip:
                    doc.strip
            numbers_str = re.findall(r"\d+", document_file)
            numbers = []
            for num_str in numbers_str:
                numbers.append(int(num_str))
            total = sum(numbers)
            average = total // len(numbers)
            print(f"Список працівників: {document_info}")
            print(f"Заробітня плата працівників: {numbers}")
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
            return total, average         
    except FileNotFoundError:
        print("Документ не знайдено!")
        return None, None


total, average = total_salary('document.txt') 
