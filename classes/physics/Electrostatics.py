from pathlib import Path
from classes.physics.Physics import Physics


class Electrostatics(Physics):

    def __init__(self):
        data_folder = Path("classes/physics/data/")
        self.file_to_open = data_folder / "electrostatics.txt"

    def getFile(self):
        return self.file_to_open