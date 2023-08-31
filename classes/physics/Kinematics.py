from pathlib import Path
from classes.physics.Physics import Physics


class Kinematics(Physics):

    def __init__(self):
        data_folder = Path("data/")
        self.file_to_open = data_folder / "kinematics.txt"

    def getFile(self):
        return self.file_to_open

    # открытие файлка
    # выбор задания
    # решение пользователя
    # сохранения ответа в файл
