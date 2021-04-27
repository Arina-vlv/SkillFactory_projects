import numpy as np

number = np.random.randint(1, 101)  # компьютер загадал рандомное число от 1 до 100
print("Загадано число от 1 до 100")

def game_core_v3(number):
    """Определяем середину диапазона (S) и сравниваем ее значение с загаданными числом (X).
    Если S > X, то поиск осуществляется во второй половине диапазоне, иначе — в первой.
    Функция принимает загаданное число и возвращает кол-во попыток"""
    count = 1              # счетчик попыток
    min = 1                # нижняя граница первоначального диапазона
    max = 100              # верхняя граница первоначального диапазона
    predict = 50           # середина первоначального диапазона
    while number != predict:
        count += 1
        if number > predict:
            print(f"Производим поиск в диапазоне [{min}; {max}]")
            print(f"Загаданное число больше {predict}")
            print("-------------")
            min = predict + 1
            predict = int((min + max) / 2)     # середина нового диапазона
        elif number < predict:
            print(f"Производим поиск в диапазоне [{min}; {max}]")
            print(f"Загаданное число меньше {predict}")
            print("-------------")
            max = predict - 1
            predict = int((min + max) / 2)
    return count         # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Загаданное число: {number}")
    print(f"Ваш алгоритм в среднем угадывает число за {score} попыток")
    return score

score_game(game_core_v3)