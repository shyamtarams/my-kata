map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
       (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def solution(n):
    r = []
    for (arabic, roman) in map:
        (f, n) = divmod(n, arabic)
        r.append(roman * f)
    return "".join(r)


print(solution(21))