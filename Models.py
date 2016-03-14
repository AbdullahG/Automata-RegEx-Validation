global counter
counter = 0

class State:
    name = ""

    acceptance = False

    def __init__(self):
        self.zero = State
        self.one = State
        self.setName()

    def setName(self):
        global counter
        self.name = "q" + str(counter)
        counter += 1


class DFA:
    start = State()
    def isValid(self,inp, ss):
        for i in range(len(inp)):
            o = "from: " + ss.name
            if inp[i] is "0":
                ss = ss.zero
            elif inp[i] is "1":
                ss = ss.one
            else:
                print(inp + " is invalid")
                return False
            o = o + " to: " + ss.name + " mov: " + inp[i]

        return ss.acceptance

    def constructDFA(self,regex, s):
        reject = State()
        reject.name = "reject"
        reject.one = reject
        reject.zero = reject

        c = 0
        for i in regex:
            if c + 1 < len(regex):
                if regex[c + 1] is "*":
                    if i is "0":
                        s.zero = s
                    elif i is "1":
                        s.one = s
                else:
                    if i is "0":
                        s.zero = State()
                        if c - 2 >= 0 and (regex[c - 1] is not "*" and regex[c - 2] is not "1"):
                            s.one = reject
                        elif c - 2 < 0:
                            s.one = reject
                        s = s.zero
                    elif i is "1":
                        s.one = State()
                        if c - 2 >= 0 and (regex[c - 1] is not "*" and regex[c - 2] is not "0"):
                            s.zero = reject
                        elif c - 2 < 0:
                            s.zero = reject
                        s = s.one
            else:
                if i is "0":
                    s.zero = State()
                    if c - 2 >= 0 and (regex[c - 1] is not "*" and regex[c - 2] is not "1"):
                        s.one = reject
                    elif c - 2 < 0:
                        s.one = reject
                    s = s.zero
                    s.one = reject
                    s.zero = reject
                elif i is "1":
                    s.one = State()
                    if c - 2 >= 0 and (regex[c - 1] is not "*" and regex[c - 2] is not "0"):
                        s.zero = reject
                    elif c - 2 < 0:
                        s.zero = reject
                    s = s.one
                    s.one = reject
                    s.zero = reject
            if c + 1 is len(regex):
                s.acceptance = True
            c += 1



