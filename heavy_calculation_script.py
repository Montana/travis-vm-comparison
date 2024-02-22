def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_primes(limit):

    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

if __name__ == "__main__":
    limit = 100000  
    print(f"Calculating prime numbers up to {limit}...")
    primes = calculate_primes(limit)
    print(f"Found {len(primes)} prime numbers up to {limit}.")
