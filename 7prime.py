def isprime(number, primes):
    for prime in primes:
        if number % prime == 0:
            return False
    return True

list_primes = [2]
counter = 3
while len(list_primes) < 10001:
    if isprime(counter, list_primes):
        list_primes.append(counter)
    counter += 1

print(list_primes.pop())
