

def find_prime_factors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2

    if n > 1:
        factors.append(n)
    return factors

def main():
    try:
        num = int(input("Enter a number to find its prime factors: "))
        
        if num < 2:
            print("Please enter a number greater than 1.")
            return
        
        prime_factors = find_prime_factors(num)
        
        print(f"\nPrime factors of {num}: {prime_factors}")
        print(f"Prime factorization: {' × '.join(map(str, prime_factors))}")
        
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()

