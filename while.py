

base_question = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}


def ask_user(list_question):
    bot_response = ''
    while True:
        user_input = input(">").lower()
        print(user_input)
        for bot_answer in list_question:
            if user_input == 'пока':
                print('Прощай')
                return
            elif user_input == bot_answer.lower():
                bot_response = (list_question[bot_answer])
                break
            else:
                bot_response = 'Не знаю'
        print(bot_response)


ask_user(base_question)
