#this program doesn't work (too slow)

def sqsum(number):
    if number == 0:
        return 0
    ans = number
    while ans != 1 and ans != 89:
        ans = sum([int(x)**2 for x in str(ans)])
    return ans

def next_1(number):
    while True:
        if sqsum(number) == 1:
            yield number
        number += 1

total = 0
for i in next_1(1):
    if i < 10000000:
        total += 1
        print(i)
    else:
        print(total)
        break
