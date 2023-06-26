def prime_status(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return "Prime" if len(divisors) == 2 else "Not Prime"
number = int(input("Enter any number to check if it is prime : "))
print(prime_status(number))