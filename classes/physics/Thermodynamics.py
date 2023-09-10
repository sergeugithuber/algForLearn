from pathlib import Path
from classes.physics.Physics import Physics


class Thermodynamics(Physics):

    def __init__(self):
        data_folder = Path("classes/physics/data/")
        self.file_to_open = data_folder / "thermodynamics.txt"

    def getFile(self):
        return self.file_to_open