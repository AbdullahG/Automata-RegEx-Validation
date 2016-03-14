import random
from Models import *
class Test:
    testList = []
    def createTestSamples(self,regex):
        while len(self.testList) < 50:
            n = random.randint(len(regex)-2,len(regex)+1)
            s = ""
            for i in range(n):
                num = random.randint(0,1)
                s = s + str(num)
            if self.testList.count(s) is 0:
                self.testList.append(s)

    def runTest(self,dfa,regex):
        self.createTestSamples(regex)
        dfa.constructDFA(regex,DFA.start)
        for i in self.testList:
            if dfa.isValid(i,DFA.start):
                print(i+" is VALID")
            else:
                print(i+" is INVALID")


