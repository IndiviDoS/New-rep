import math
# def pi(n):
#     p = math.pi
#     x = str(p)
#     for i in range(1,n+1):
#         print(x[i])
# pi(int(input()))

# def divided_3_4(n): 
#     for i in range(0, n+1):  
#         x = str(math.pi)        
#         yield x[i]
# n = int(input()) 
# a = divided_3_4(n) 
# for j in divided_3_4(n): 
#     print(next(a), end='') 
import json 
with open("sample_data.json", "r") as my_file: 
    json_string = my_file.read() 
data = json.loads(json_string) 
z = data.get('gpa','')
w = data.get('email',{})
