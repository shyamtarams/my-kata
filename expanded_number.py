def expanded_form(num):
    rslt = []
    for i, n in enumerate(str(num)[::-1]):
        if int(n) != 0: rslt.append(n + ('0' * i))
    return ' + '.join(rslt[::-1])
print("expanded format : ",expanded_form(123))