#1
def ouncetogramm(gramm):
    ounce = gramm * 29.3495231
    return ounce
g = int(input())
o = ouncetogramm(g)
print(f"{o} ounces")

#2
def c(f):
    cel = (5/9) * (f - 32)
    return cel
ff = int(input())
cc = c(ff)
print(f"{cc} celcius")

#3
def solve(numheads,numlegs):
    c = numheads -(numlegs - (numheads * 2))/2
    r = (numlegs - (2 * numheads))/2
    return c ,r 
h = int(input())
l = int(input())
ch ,ra = solve(h,l)
print(f"{ch} chickens, {ra} rabbits")

#4
def isPrime(num):
    cnt = 0
    for i in range(1, num + 1):
            if num % i == 0:
                cnt = cnt + 1
    return cnt == 2

result2 = [x for x in map(int, input().split()) if isPrime(x)]#comprehension of list
print(result2)

#5
