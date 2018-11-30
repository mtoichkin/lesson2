def get_summ(num_one, num_two):
    num_sum = None
    try:
        num_sum = int(num_one)+int(num_two)
    except ValueError:
        print('ValueError - num_one:', type(num_one), "num_two:", type(num_two))
    return num_sum


print(get_summ(22.3, "22.e"))
