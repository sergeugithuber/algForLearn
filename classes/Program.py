def start():
    print("program is on")
    key = chooseItem()
    if key == None: return None
    startTesting(key)
    


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

def startTesting(key):
    # Сдесь можно добавить функцию выбора кол-ва заданий
    if key == 1:
    
        
