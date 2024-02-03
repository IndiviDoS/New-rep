def isPrime(num):
    cnt = 0
    for i in range(1, num + 1):
            if num % i == 0:
                cnt = cnt + 1
    return cnt == 2

result2 = [x for x in map(int, input().split()) if isPrime(x)]#comprehension of list
print(result2)