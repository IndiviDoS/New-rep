numbers = []
nums = list(map(int,input().split()))
numbers.extend(nums)
prime_nums = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1, numbers))
print("Prime numbers in the list:", prime_nums)