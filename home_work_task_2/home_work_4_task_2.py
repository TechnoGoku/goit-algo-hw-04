from pathlib import Path
from pprint import pprint

def get_cats_info(path) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as pets:
            pets_file = pets.read()
            lines_n = pets_file.split('\n')
            pets_list_info = []
            for line in lines_n:
                lines = line.split(',')
                pets_list_info.extend(lines)
            pets_list = []
            for i in range(0, len(pets_list_info), 3):
                if i + 2 < len(pets_list_info):
                    pet_id = pets_list_info[i]
                    pet_name = pets_list_info[i+1]
                    pet_age = pets_list_info[i+2]
                    pets_list.append({'id': pet_id, 'name': pet_name, 'age': pet_age, })
            
            return pets_list
    except FileNotFoundError:
        print("Документ не знайдено!")



cats_info = get_cats_info("C:/Users/User/Desktop/home_work_4/home_work_task_2/pets.txt")
pprint(cats_info)




