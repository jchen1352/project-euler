import time
time.clock()

MAX_NUMBER = 2000000
num_list = [x for x in range(2,MAX_NUMBER)]
index = 0
while index < len(num_list) - 1:
    if num_list[index] != 0:
        current_prime = num_list[index]
        for i in range(index + current_prime, len(num_list), current_prime):
            num_list[i] = 0
    index += 1
print(sum(num_list))

print("Time elapsed: "+str(time.clock()) +" s.")
