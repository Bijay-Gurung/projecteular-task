# Largest prime factor
"""
Program to find the largest prime factor of the number 600851475143
"""

def largestPrimeNumber(num):
    count = 0
    multiValue = 0
    for i in range(1,1000):
        if num % i == 0:
            print(i)
        count = count + i
        multiValue = count * count
        if multiValue == num:
            break
        else:
            continue
largestPrimeNumber(13195)