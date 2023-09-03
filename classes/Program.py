def start():
    print("program is on")
    key = chooseItem()
    if chooseItem() == None: return None
    countOfTask()
    i = 0
    while i != countOfTask():
        i = i + 1
        randTask()
    
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
    