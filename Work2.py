#Emmanuel Bassey BHU/19/04/02/0005
# Largest number in a list
numbers = [1, 2, 345, 4, 5]
largest = max(numbers)
print(largest)

# Print prime numbers from 0 to n
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_prime_numbers(n):
    print("Prime numbers from 0 to", n, ":")
    for number in range(2, n + 1):
        if is_prime(number):
            print(number)

n = int(input("Enter a number: "))

print_prime_numbers(n)

# Reverse numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
numbers.reverse()
print(numbers)

# Sum of numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(numbers))

# Print even numbers between 4 and 30
numbers = range(4, 30, 2)
for number in numbers:
    print(number)
