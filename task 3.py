def largest_prime_factor(num):
    largestPrimeFactor = 1
    for i in range(2,int(num**0.5)+1):
        while num%i == 0:
            largestPrimeFactor = i
            num //= i
    if num > largestPrimeFactor:
        largestPrimeFactor = num
    return largestPrimeFactor
result = largest_prime_factor(600851475143)
print(result)