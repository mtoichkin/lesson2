def compare_str(str1,str2):
    compare_result = None
    if type(str1) == str and type(str2) == str:
        if str1 == str2:
            compare_result = 1
        else:
            if str2 == 'learn':
                compare_result = 3
            elif len(str1) > len(str2):
                compare_result = 2
    else:
        compare_result = 0
    return compare_result

print(compare_str(1,"leassrn"))
print(compare_str("sss","sss"))
print(compare_str("ssssssss","ddwr"))
print(compare_str("sss","learn"))
print(compare_str("sss","leassrn"))