def num_factors(number):
    count = 0
    root = number**.5
    for i in range(1,int(root)+1):
        if number % i == 0:
            if i == root:
                count += 1
            else:
                count += 2
    return count

index = 1
factors = 0
while factors <= 500:
    triangular = index * (index+1) / 2
    factors = num_factors(triangular)
    index += 1
print(triangular)
