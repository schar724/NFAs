#######################################
# Lab code for COMP 2613, Fall 2022
# Janet Leahy
# Oct. 20, 2022
#######################################


from asyncio.windows_events import NULL
from typing_extensions import Self


class State:
    def __init__(self, suc, transitions = []):
        self.success = suc                  # boolean indicating whether State is a success state
        self.transitions = transitions     # nextStates is array of (char, State) tuples capturing the outgoing transitions
        print(f"Created State representing with {len(self.transitions)} output transitions and success = {self.success}.")

def epsilonClosure(nfa):
    epsilonStates = nfa.copy()
    checkStates = nfa.copy()
    while len(checkStates) > 0:
        currentState = checkStates.pop()
        for transition in currentState.transitions:
            if transition[0] == "eps" and transition[1] not in epsilonStates:
                epsilonStates.append(transition[1])
                checkStates.append(transition[1])
    return epsilonStates
                

    
    

# build NFA
        
q3 = State(True, [])        
q2 = State(False, [("c", q3)])        
q1 = State(False, [("b", q3)])
q1.transitions.append(("b",q1))
q0 = State(False, [("a", q1),("a", q2),("eps", q3)])
q3.transitions.append(("eps",q2))
# q2.transitions.append(("eps", q0))

nfa = q0

# run NFA

instr = ""
print(f"Input string: {instr}")

## TO DO

currentState = [nfa]

currentState = epsilonClosure(currentState)
print(f"Start State: {currentState}")
for char in instr:
    nextState = []
    print(f"next state: {nextState}")
    for state in currentState:
        for transition in state.transitions:
            if(transition[0] == char):
                nextState.append(transition[1]) 

    nextState = epsilonClosure(nextState)
    
    currentState = nextState

for state in currentState:
    if(state.success):
        print("YAY!!!")
    

           