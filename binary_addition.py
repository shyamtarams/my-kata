def add_binary(a,b):
    s = a + b
    return bin(s).strip()[2:]
print(add_binary(1,1))