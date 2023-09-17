from random import randint

class Physics:

    def chooseUnderItem(self):
        r = randint(0, self.len_dict)
        return self.dict.get(r)
    
    def chooseTask(self, fileName):
        # Нахождение размера файла
        with open(fileName, "r", encoding="UTF-8") as f:
            array = f.readlines()
            # выбор случайного числа
            num = randint(1, len(array) - 1)
            if int(num % 2) == 0:
                num = num + 1

        with open(fileName, "r", encoding="UTF-8") as f:
            i = 0
            for line in f:
                if i == num - 1:
                    print("Задача:")
                    print(line)
                    print("Ответ: ")
                if i == num:
                    answer = line.split()
                    answer = answer[0]
                    break
                i = i + 1
        # вернуть ответ и даллее сверить с пользовательским
        print("Ответ:")
        answerUser = int(input())
        if answer == answerUser:
            print("Верно!")
        return answer
