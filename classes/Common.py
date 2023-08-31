from classes.physics.Physics import Physics
from classes.physics.Kinematics import Kinematics
from classes.physics.Dynamics import Dynamics

k = Kinematics()
d = Dynamics()
dict = {0 : k.getFile,
            1 : d.file_to_open
                }
len_dict = len(dict)