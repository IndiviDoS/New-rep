msg= "Hello"
def isPrime(num):
    cnt = 0
    for i in range(1, num + 1):
            if num % i == 0:
                cnt = cnt + 1
    return cnt == 2

def filter_prime(nums):
    primes = []
    for num in nums:
        if isPrime(num):
            primes.append(num)
    return primes

result = filter_prime(map(int, input().split()))
result2 = [x for x in map(int, input().split()) if isPrime(x)]#comprehension of list
print(result)
print(result2)