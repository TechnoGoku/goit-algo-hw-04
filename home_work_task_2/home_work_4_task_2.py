from pathlib import Path

def get_cats_info(path):
    pets_list = []
    with open(path, 'r', encoding='utf-8') as pets:
        pets_file = pets.read()
        lines_n = pets_file.split('\n')
        pets_list_info = []
        for line in lines_n:
            lines = line.split(',')
            pets_list_info.extend(lines)
        print(pets_file)
        print(pets_list_info)



cats_info = get_cats_info("C:/Users/User/Desktop/home_work_4/home_work_task_2/pets.txt")
# print(cats_info)