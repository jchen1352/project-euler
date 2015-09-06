def factor(number):
    factors = []
    factor = 2
    while number > 1:
        if number % factor == 0:
            factors.append(factor)
            number = number / factor
            factor = 2
        else:
            factor += 1
    return factors

palin_list = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            palin_list.append(100001*x+10010*y+1100*z)
            palin_list.append(10001*x+1010*y+100*z)

'''
for palin in palin_list:
    palin_factors = factor(palin)
    if len(palin_factors) == 2:
        if len(str(palin_factors[0])) == 3 and len(str(palin_factors[1])) == 3:
            print(palin, palin_factors)
'''

for x in range(900,1000):
    for y in range(900,1000):
        xy = x*y
        if xy in palin_list:
            print(xy)
