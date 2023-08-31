from pathlib import Path
from classes.Program import start
from classes.physics.Kinematics import Kinematics

# Запуск программы
# start()


#########
### ЗДЕСЬ Я ПРИШЕЛ К ТОМУ ЧТО НУЖНО ДЕЛАТЬ ПУТЬ К ФАЙЛУ ОТНОСИТЕЛЬНО MAIN.py
k = Kinematics()
print(k.file_to_open)

data_folder = Path("classes/physics/data")
file_to_open = data_folder / "kinematics.txt"
k.file_to_open = file_to_open

k.chooseTask(k.file_to_open)

#################