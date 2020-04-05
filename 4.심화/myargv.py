import sys
sum = 0
for i in sys.argv:
    if type(i)==int:
        sum = sum+i
print(sum)