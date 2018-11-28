

base_question = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}


def ask_user(questions):
    try:
        bot_response = ''
        while True:
            user_input = input(">").lower()
            for question in questions:
                if user_input == 'пока':
                    print('Прощай')
                    return
                elif user_input == question.lower():
                    bot_response = (questions[question])
                    break
                else:
                    bot_response = 'Не знаю'
            print(bot_response)
    except KeyboardInterrupt:
        print("Пока!")
        return


ask_user(base_question)
