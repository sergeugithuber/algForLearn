from classes.physics.Physics import Physics
from random import randint
from classes.physics.Kinematics import Kinematics
from classes.physics.Dynamics import Dynamics
from classes.physics.Molecular import Molecular
from classes.physics.Electrostatics import Electrostatics
from classes.physics.Thermodynamics import Thermodynamics

# Запуск основной программы


def start():
    print("program is on")
    key = chooseItem()
    if chooseItem() == None:
        return None
    countOfTask()
    i = 0
    while i != countOfTask():
        i = i + 1
        # randTask()

# Выбор предмета Физика, Русский, Математика и т.д.. На данный момент доступна только Физика


def chooseItem():
    print("Выберите предмет")
    print("[1] - Физика\n[0] - Выход")
    key = input()

    while True:

        if key == "1":
            # Выбрана Физика
            return 1

        if key == "0":
            return None  # Выход

        else:
            print("Неизвестная кнопка")

        print("Выберите предмет")
        key = input()

# Выбор кол-ва заданий мин. 1, макс. 10


def countOfTask():
    print("Введи кол-во заданий(макс. 10):")
    while True:
        count = int(input())
        if count <= 10 and 1 < count:
            return count
        print("---")

# Выбор ПОДпредмета выбронного предмета


def randChapter():
    p = Physics()
    p.chooseTask(returnPhysicsTask())


def returnPhysicsTask():
    k = Kinematics()
    d = Dynamics()
    m = Molecular()
    e = Electrostatics()
    t = Thermodynamics()
    dictPhysics = {
        1 : k.getFile(),
        2 : d.getFile(),
        3 : m.getFile(),
        4 : e.getFile(),
        5 : t.getFile()
    }

    r = randint(1, len(dictPhysics))
    return dictPhysics.get(r)