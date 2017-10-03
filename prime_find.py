# returns a list of prime numbers up to the integer n
# n is integer
# int -> list of int


def prime_find(n):
    prime_list = []
    for i in range(1, n):
        if is_prime(i):
            prime_list.append(i)
    if prime_list[0] == 1:  # to account for one not being a prime number
        prime_list = prime_list[1:]
    return prime_list


def is_prime(num):  # checks if a number is prime
    for j in range(1, num):
        if num % j == 0 and j != 1:
            return False
    return True

