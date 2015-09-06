import time
def get_collatz(start):
    sequence = [start]
    while start != 1:
        if start % 2 == 0:
            start = int(start / 2)
        elif start % 2 == 1:
            start = start * 3 + 1
        sequence.append(start)

    return sequence
time.clock()
#taken = set()
#evens = set([x for x in range(2,1000000,2)])
longest = 0
longest_start = 0
for i in range(999999,3,-2):
    sequence = get_collatz(i)
    length = len(sequence)
    if length > longest:
        longest = length
        longest_start = i
        print(longest_start)
        #taken = (taken | set(sequence))

print(longest_start)
print(time.clock())
