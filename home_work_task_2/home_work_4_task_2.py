from pathlib import Path

def get_cats_info(path):
    with open(path, 'r', encoding='utf-8') as pets:
        pets_file = pets.read()
        print(pets_file)



cats_info = get_cats_info("C:/Users/User/Desktop/home_work_4/home_work_task_2/pets.txt")
# print(cats_info)