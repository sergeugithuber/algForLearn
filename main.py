# from pathlib import Path
# from classes.Program import start
# from classes.physics.Kinematics import Kinematics
from classes.Program import randChapter, start

# Запуск программы
# start()


#########
### ЗДЕСЬ Я ПРИШЕЛ К ТОМУ ЧТО НУЖНО ДЕЛАТЬ ПУТЬ К ФАЙЛУ ОТНОСИТЕЛЬНО MAIN.py
# k = Kinematics()
# print(k.file_to_open)

# data_folder = Path("classes/physics/data")
# file_to_open = data_folder / "kinematics.txt"
# k.file_to_open = file_to_open

# k.chooseTask(k.file_to_open)

#################

from random import randint


dict = {
    1 : "k1",
    2 : "k2",
    3 : "k3",
    4 : "k4",
    5 : "k5",
    6 : "k6"
}


for x in range(0, 10):
    r = randint(1, len(dict))
    print(dict.get(r))
    x = x + 1


import random
r = random.randint(1, 100)
if r >= 75:
    print(f'Ты проиграл, твой шанс: {r}') 
elif r <= 35:
    print(f'Ты выиграл, твой шанс: {r}') 

start()
