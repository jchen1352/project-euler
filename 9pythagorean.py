def get_triple(m,n):
    return [n**2-m**2, 2*m*n, m**2+n**2]

a = 1
b = 2
while a < 1000:
    while b < 1000:
        triple = get_triple(a,b)
        triple_sum = sum(triple)
        if 1000 % triple_sum == 0 or triple_sum > 1000:
            break
        b+=1
    if triple_sum > 1000:
        a += 1
        b = a + 1
    if 1000 % triple_sum == 0:
        break
print(triple)
