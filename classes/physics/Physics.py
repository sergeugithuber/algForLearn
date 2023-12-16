from random import randint

class Physics:

    def chooseUnderItem(self):
        r = randint(0, self.len_dict)
        return self.dict.get(r)
    
    def chooseTask(self, fileName):
        with open(fileName, "r", encoding="UTF-8") as f:
            array = f.readlines()
            num = randint(1, len(array) - 1) # выбор случайного числа
            if int(num % 2) == 0:
                num = num + 1

        with open(fileName, "r", encoding="UTF-8") as f:
            i = 0
            for line in f:
                if i == num - 1:
                    print("-------------\nЗадача:")
                    print(line)
                if i == num:
                    answer = line.split()
                    answer = answer[0]
                    break
                i = i + 1
        answerUser = input("Ответ: ")
        print("результат: ", end="")
        if answer == answerUser:
            print("ВЕРНО!")
        else:
            print("НЕверно")
        return answer
