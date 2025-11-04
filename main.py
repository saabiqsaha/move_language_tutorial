

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
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        if num1 < 2 or num2 < 2:
            print("Please enter numbers greater than 1.")
            return
        
        prime_factors1 = find_prime_factors(num1)
        prime_factors2 = find_prime_factors(num2)
        
        print(f"\nThe Prime factors of {num1} are {prime_factors1}")
        print(f"and the prime factorization is {' × '.join(map(str, prime_factors1))}")
        
        print(f"\nThe Prime factors of {num2} are {prime_factors2}")
        print(f"and the prime factorization is {' × '.join(map(str, prime_factors2))}")
        
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()

