# f = 1
# fi = 1
# n = int(input())
# for i in range(n):
#     f_sum = f + fi
#     f = fi
#     fi = f_sum
# print(fi)

st = input()
sum = 0
for i in range (0,len(st)):
    if st[i].isdigit() == True:
        lo = int(st[i])
        sum = sum + lo
print(sum)