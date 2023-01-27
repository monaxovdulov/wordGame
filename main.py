score_player1 = 0
score_player2 = 0

user_word = input('игрок 1 начинает игру и вводит любое слово\n чтобы выйти из игры введите команду stop').lower()
used_words = [user_word]
counter = 1
while user_word != "stop":
    print(f"Счёт игроков\nИгрок 1 - {score_player1}\nИгрок 2 - {score_player2}\n")
    print("Слова которые уже были", used_words)
    last_letter = user_word[-1]
    if not (last_letter in "ячсмитбюэждлорпавфйцукенгшщзхё"):
        last_letter = user_word[-2]

    user_word = input(f'Игрок {counter % 2 + 1} вводите слово на букву "{last_letter}"').lower()
    while user_word in used_words:
        print(f'СЛОВО {user_word} уже было введите другое')
        user_word = input(f'Игрок {counter % 2 + 1} вводите слово на букву "{last_letter}"').lower()
    while user_word[0] != last_letter:
        print(f"Предыдущее слово не начинается на букву '{user_word[0]}', пожалуйста введите букву начинающуюся на {last_letter} ")
        user_word = input(f'Игрок {counter % 2 + 1} вводите слово на букву "{last_letter}"').lower()

    if counter % 2 == 0:
        score_player1 = score_player1 + 10
    else:
        score_player2 = score_player1 + 10

    counter += 1
    used_words.append(user_word)
