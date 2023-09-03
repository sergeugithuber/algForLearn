from pathlib import Path
from classes.physics.Physics import Physics


class Molecular(Physics):

    def __init__(self):
        data_folder = Path("data/")
        self.file_to_open = data_folder / "molecular.txt"

    def getFile(self):
        return self.file_to_open