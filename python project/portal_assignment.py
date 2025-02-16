# from math import sqrt

# def print_primes(n):
#     if n <= 0:
#         print("Invalid input. n must be greater than 0.")
#         return
    
#     for num in range(2, n + 1):  # Start from 2 since 1 is not a prime number
#         is_prime = True
#         for i in range(2, int(sqrt(num)) + 1):  # Check divisors up to the square root of num
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)

#  # Given input
# n = 10
# print_primes(n)


# n=4
# def print_pattern(n):
#     for i in range(n, 0, -1):
#         print('*' * i)

# print_pattern(n)


# def print_floyds_triangle(n):
#     current_number = 1
#     for i in range(1, n + 1):
#         for j in range(i):
#             print(current_number, end='')
#             current_number += 1
#         print()

# n = 4
# print_floyds_triangle(n)

# def number_pattern(n):
#     for i in range(1, n + 1):
#         for j in range(i):
#             print(i, end='')
#         print()

# n = 4
# number_pattern(n)
