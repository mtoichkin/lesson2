
school_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2, 3]},
                 {'school_class': '4b', 'scores': [3, 4, 4, 5, 2, 5, 5]},
                 {'school_class': '5a', 'scores': [3, 4, 5, 5, 2, 4, 3, 3, 5, 5]},
                 {'school_class': '5b', 'scores': [3, 4, 4, 5, 2]},
                 {'school_class': '6a', 'scores': [3, 4, 4, 5, 2, 3, 3, 4]}]


def average_scores_class(school):
    class_average_scores = {}
    for class_number in school:
        class_learners_average_scores = 0
        for learners_scores in class_number['scores']:
            class_learners_average_scores = class_learners_average_scores+learners_scores
        class_average_scores[(class_number['school_class'])] = class_learners_average_scores/len(class_number['scores'])
    return class_average_scores

def average_scores_school_print(school):
    school = average_scores_class(school)
    school_average_scores = 0
    for class_number in school:
        school_average_scores = school_average_scores + school[class_number]
    return print("Средний балл по всей школе", school_average_scores/len(school))

def average_scores_class_print(school):
    school_class = average_scores_class(school)
    for class_number in school_class:
        print("средний балл по классу", class_number, school_class[class_number])


average_scores_school_print(school_scores)

average_scores_class_print(school_scores)

