def sting(string):
    list = []
    for word in string:
        list.append(word)
    return list
result = sting(input().split())
print(sorted(result))