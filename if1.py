def user_age():
    try:
        age = int(float(input('Сколько вам лет:')))
        if age <= 0:
            print("Не может быть <= 0")
        return age
    except (ValueError, TypeError):
        print("Введено не число")


def user_occupation(age):
    try:
        occupation = ""
        if age is None:
            occupation = "Возраст не получен"
        elif 0 < age < 6:
            occupation = "Детский сад"
        elif 6 <= age < 18:
            occupation = "Школа"
        elif 18 <= age < 23:
            occupation = "ВУЗ"
        elif 23 <= age:
            occupation = "Работа"
    except (ValueError, TypeError):
        print("Введено не число")
    return occupation

print(user_occupation(user_age()))
