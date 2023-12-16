from classes.physics.Physics import Physics
from random import randint
from classes.physics.Kinematics import Kinematics
from classes.physics.Dynamics import Dynamics
from classes.physics.Molecular import Molecular
from classes.physics.Electrostatics import Electrostatics
from classes.physics.Thermodynamics import Thermodynamics

def start(): # запуск алгоритма
    while True:
        if chooseItem() == None:
            return None
    
        count = countOfTask()
        i = 0
        while i != count:
            i = i + 1
            randChapter()

def chooseItem(): # выбор раздела
    print("[1] - Физика\n[0] - Выход")
    key = input("Выберите предмет: ")

    while True:
        if key == "1":
            # Физика
            return 1

        if key == "0":
            print("bye")
            return None  # Выход
        else:
            print("Неизвестная кнопка")

        print("Выберите предмет")
        key = input()

# Выбор кол-ва заданий мин. 1, макс. 10


def countOfTask(): # выбор количества заданий
    print("Введи кол-во заданий(макс. 10):")
    while True:
        count = int(input())
        if count <= 10 and 1 <= count:
            return count
        print("---")

def randChapter():
    p = Physics()
    p.chooseTask(returnPhysicsTask())

def returnPhysicsTask(): # случайный выбор задачи из подраздела физики
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