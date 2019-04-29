def is_isogram(string):
    str = string.lower()
    lttrs = []
    for lttr in str:
        if lttr.isalpha():
            if lttr in lttrs:
                return False
        lttrs.append(lttr)
    return True


print(is_isogram("abc"))