from Models import *
from test import *


reg2 = "0*111*0001*0*"

dfa = DFA()
dfa.constructDFA(reg2,DFA.start)

testList = []

i1 = "011100010"
i2 = "110000"
i3 = "111110000"
i4 = "1111000110"

testList.append(i1)
testList.append(i2)
testList.append(i3)
testList.append(i4)

for i in testList:
    try:
        if dfa.isValid(i,DFA.start):
            print(i+" is VALID")
        else:
            print(i+" is INVALID")
    except:
        print(i+" is not applicable")


