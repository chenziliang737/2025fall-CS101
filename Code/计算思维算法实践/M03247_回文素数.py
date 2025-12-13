import math


def is_prime(num):
    if num < 2:
        return False
    if num in {2, 3, 5, 7}:
        return True
    if num % 2 == 0 or num % 5 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def generate_palindromes(n):
    palindromes = []
    if n == 1:
        return [2, 3, 5, 7]
    half_len = (n + 1) // 2
    start, end = 10 ** (half_len - 1), 10**half_len
    for first_half in range(start, end):
        first_half_str = str(first_half)
        if n % 2 == 0:
            palindrome = int(first_half_str + first_half_str[::-1])
        else:
            palindrome = int(first_half_str + first_half_str[:-1][::-1])
        if is_prime(palindrome):
            palindromes.append(palindrome)
    return palindromes


def find_palindromic_primes(n):
    primes = generate_palindromes(n)
    print(len(primes))
    print(" ".join(map(str, primes)))


n = int(input().strip())
find_palindromic_primes(n)
