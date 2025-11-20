X= {19,7,21,99,5, 18, 11, 60,31,99, 105, 4, 2} 


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
    
def select_prime_numbers(X):
    prime_numbers = []
    for number in X:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

print(select_prime_numbers(X))