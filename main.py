DESCRIPTION_GAME = """
Описание программы "Игра в слова"
Играют два игрока
у каждого в начале по 10 очков
Первым ходит игрок с номером 1
Он вводит любое слово (не получает за это очков)
Далее следующий игрок вводит слово,
которое должно начинаться на последнюю букву предыдущего слова
после тоже самое делает игрок 1
если игроки вводят слова коректно то получают очки, а
иначе их количество очков уменьшается
Игра продолжается до тех пор пока кто-то нибудь не ввеет слово 'stop'
или пока у игроков положительный счёт
"""
print(DESCRIPTION_GAME)

# здесь будет хранится количесво очков у игроков
score_player1 = 10
score_player2 = 10

game_over = False

print(f"Счёт игроков\nИгрок 1 - {score_player1}\nИгрок 2 - {score_player2}\n")
user_word = input('игрок 1 начинает игру и вводит любое слово\n чтобы выйти из игры введите команду stop:').lower()

while user_word == "":
    print("Ты не ввел никакого слова попробуй ещё раз")
    user_word = input('Вводить сюда:').lower()

is_an_invalid_char = True
while is_an_invalid_char:
    for char in user_word:
        if char not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print(f"Недопустимый символ {char} ")
            user_word = input('Введите слово еще\nВводить сюда:').lower()
            break
    else:
        is_an_invalid_char = False

used_words = [user_word]  # список уже использованных слов, сразу создаем с первым словом word
counter = 1  # перемнная счётчик, для того чтобы в цикле игроки шли по очереди

# код ниже будет выполняться до тех пор пока игрок не введет слово "stop" или пока у игроков положительный счёт
while user_word != "stop" and score_player1 > 0 and score_player2 > 0:
    print("Слова которые уже были", used_words)
    while user_word == "":
        print("Ты не ввел никакого слова попробуй ещё раз")
        user_word = input('Вводить сюда:').lower()

    last_letter = user_word[-1]  # делаем срез строки по индексу [-1]  чтобы получить последнюю букву
    if not (last_letter in "ячсмитбюэждлорпавфйцукенгшщзхё"):  # если последняя буква не входит в "ячсм..."
        last_letter = user_word[-2]  # то в берем предпоследнюю букву

    # counter%2 получаем остаток от деления counter на 2
    # если число четное, остаток будет 0 и это ход игрока 1 ,
    # а если число нечетное то остаток будет 1  и это ход игрока 2
    user_word = input(f'Игрок {counter % 2 + 1} вводите слово на букву "{last_letter}"').lower()

    # пока загаданное слово входит в список уже использованных слов
    while user_word in used_words:
        if score_player1 < 0 or score_player2 < 0:
            print("Вы потратили все очки")
            game_over = True
            break
        print(f'СЛОВО {user_word} уже было введите другое')
        if counter % 2 == 0:
            score_player1 = score_player1 - 5
            print("-5")
        else:
            score_player2 = score_player2 - 5
            print("-5")

        user_word = input(f'Игрок {counter % 2 + 1} вводите слово на букву "{last_letter}"').lower()

    if game_over:
        continue

    # пока первая буква введённого игроком слова не равна последней букве предыдушего слова
    while user_word[0] != last_letter:
        if score_player1 < 0 or score_player2 < 0:
            print("Вы потратили все очки")
            game_over = True
            break
        print(
            f"Предыдущее слово не начинается на букву '{user_word[0]}', пожалуйста введите букву начинающуюся на {last_letter} ")
        if counter % 2 == 0:
            score_player1 = score_player1 - 10
            print("-10")
        else:
            score_player2 = score_player2 - 10
            print("-10")
        user_word = input(f'Игрок {counter % 2 + 1} вводите слово на букву "{last_letter}"').lower()

    if game_over:
        continue

    if counter % 2 == 0:  # если это ход первого игрока то увеличиваем его счёт на 10
        score_player1 = score_player1 + 10
        print("+10")
    else:  # иначе увеличиваем счет второго игрока
        score_player2 = score_player2 + 10
        print("+10")

    counter += 1  # увеличиваем переменную counter на 1
    used_words.append(user_word)  # добавляем слово в список уже использованных слов в игре

    print(f"Счёт игроков\nИгрок 1 - {score_player1}\nИгрок 2 - {score_player2}\n")

if score_player1 > 0 and score_player1 > score_player2:
    print(f"Победил игрок 1\nЕго счёт - {score_player1}")
elif score_player2 > 0 and score_player2 > score_player1:
    print(f"Победил игрок 2\nЕго счёт - {score_player2}")
else:
    print(f"игрок 1 {score_player1}\nигрок 2{score_player2}")

