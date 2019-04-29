def countBits(n):
    count =0 #initiazing count variable
    while(n):
         count +=n & 1
         n>>=1
    return count
print(countBits(10))