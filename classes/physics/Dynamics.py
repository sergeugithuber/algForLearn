from pathlib import Path
from classes.physics.Physics import Physics


class Dynamics(Physics):

    def __init__(self):
        data_folder = Path("data/")
        self.file_to_open = data_folder / "dynamics.txt"

    def getFile(self):
        return self.file_to_open