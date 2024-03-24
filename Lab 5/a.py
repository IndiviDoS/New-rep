# import re
# """
# with open("text.txt", "r") as fp:
#     r = fp.readlines()
# s = ''.join(r)"""

s = "abba abbbbb gaag kook ajab"
d = ''.join(s)
a = re.compile("a.*b")
m = a.findall(d)
print(m)
import re
s = "abba ab,bb.bb g,.a,a.g kook ajab"
# Replace space, comma, or dot with a colon
result = re.sub(r'[ ,.]', ':', s)
print(result)