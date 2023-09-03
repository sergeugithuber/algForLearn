from random import randint
from classes.physics.Kinematics import Kinematics
from classes.physics.Dynamics import Dynamics
from classes.physics.Molecular import Molecular

class DictPhysics:

    k = Kinematics()
    d = Dynamics()
    m = Molecular()
    dictPhysics = {
        1 : k.getFile(),
        2 : d.getFile(),
        3 : m.getFile()
    }

    def __init__(self):
        pass
        
    def chooseRandFile():
        r = randint(1, len(DictPhysics.dictPhysics))
        DictPhysics.dictPhysics.get(r)
    
