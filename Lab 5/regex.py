#1
import re
def test(alo, inp, out):
    if re.search(alo, inp) == out:
        print("test is not passed")
    elif re.search(alo, inp) != None:
        print("test is passed!")
    else:
        print("test is not passed")
alo = '^a(b*).'
test(alo, "123ab45", None)

#2
def test(alo, Data, Result):
    if re.search(alo, Data) == Result:
        print("test is passed!")
    elif re.search(alo, Data) != None:
        print("test is passed!")
    else: 
        print("test is not passed!")
alo = 'ab{2,3}'

#3
def test(alo, inp, Result):
    if re.search(alo, testinput) == Result:
        print("test is passed!")
    elif re.search(alo, inp) != None:
        print("test is passed")
    else: 
        print("test is not passed!")

alo = '[a-z]_[a-z]'

#4
def test(alo, Data, Num, Result):
    if re.search(alo, Data) == Result:
        print(Num + " is passed!")
    elif re.search(alo, Data) != None:
        print(Num + " is passed!")
    else: 
        print(Num + " is not passed!")

alo = '[A-Z][a-z]'

#5
def test(alo, Data, Num, Result):
    if re.search(alo, Data) == Result:
        print(Num + " is passed!")
    elif re.search(alo, Data) != None:
        print(Num + " is passed!")
    else: 
        print(Num + " is not passed!")

alo = '^a.*b$'

#6
def test(alo, inp, out):
    result = re.sub(alo, ':', inp)
    if result == out:
        print("test is passed!")
    else:
        print("test is not passed!")

alo = '[,]|[" "]|[@]'

#7
def test(alo, inp, out):
    result = re.sub(alo, "", inp)
    if result == out:
        print("test is passed!")
    else:
        print("test is not passed!")
alo = '[_]'

#8
def test(alo, data, res):
    result = re.split(alo, data)
    print(result)
    if result == res:
        print("test is passed!")
    else: 
        print("test is not passed!")

alo = r'([A-Z][a-z]*)'

#9
def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, r"\1 \2", testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
pattern = r'(\w)([A-Z])'
test(pattern, "MySuperTest", "test1", "My Super Test")
test(pattern, " MySuperTest IAmRobot", "test2", " My Super Test I Am Robot")

#10
def test(pattern, testData, expectedResult):  
    result = re.sub(pattern, r"\1 \2", testData)  
    print(result)  
    if result == expectedResult:  
        print("test is passed!")  
    else:   
        print("test is not passed!")  
pattern = r'([a-zA-Z])([A-Z])'  
test(pattern, "MySuperTest", "My Super Test")  
test(pattern, " MySuperTest IAmRobot", " My Super Test I Am Robot")
