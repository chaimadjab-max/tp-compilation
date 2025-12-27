#chaima djaballah G02  Security
#salsabil khadar G02  Security
#Oumayma Lahmadi G02  réseau



# Constants
MAX_STATES = 20
MAX_TRANS = 50

# States & Alphabet
states = []
alphabet = []
# Transitions
# each transition: (from_state, symbol, to_state)
transitions = []

# Final states
final_states = []

# Read nfa
def read_nfa():
    global states, alphabet, transitions, final_states

    num_states = int(input("Number of states: "))
    if num_states > MAX_STATES:
        print("Too many states!")
        return

    for i in range(num_states):
        state = input(f"State {i + 1}: ")
        states.append(state)

    alpha_size = int(input("Alphabet size: "))
    for i in range(alpha_size):
        symbol = input(f"Symbol {i + 1}: ")
        alphabet.append(symbol)

    num_final = int(input("Number of final states: "))
    for i in range(num_final):
        fs = input(f"Final state {i + 1}: ")
        final_states.append(fs)

    num_trans = int(input("Number of transitions: "))
    print("Enter transitions: from symbol to (use e for epsilon)")
    for _ in range(num_trans):
        frm, sym, to = input().split()
        transitions.append((frm, sym, to))

# Check if state exists in a set

def contains(state_set, state):
    return state in state_set

# Epsilon-closure
def epsilon_closure(state):
    stack = [state]
    closure = []

    while stack:
        current = stack.pop()
        if current not in closure:
            closure.append(current)
            for (frm, sym, to) in transitions:
                if frm == current and sym == 'e':
                    stack.append(to)

    return closure
# New transitions without epsilon
def compute_new_transitions():
    print("\nTransitions:")

    for s in states:
        closure = epsilon_closure(s)

        for a in alphabet:
            result = []

            for c in closure:
                for (frm, sym, to) in transitions:
                    if frm == c and sym == a:
                        temp = epsilon_closure(to)
                        for t in temp:
                            if t not in result:
                                result.append(t)

            if result:
                print(f"δ({s}, {a}) = {{ {' '.join(result)} }}")
# New final states
def compute_new_final_states():
    new_finals = []

    for s in states:
        closure = epsilon_closure(s)
        for c in closure:
            if c in final_states:
                new_finals.append(s)
                break

    print("Final States: {", " ".join(new_finals), "}")

# Display automaton

def display_automaton():
    print("\n NFA without epsilon ")

    print("States: {", " ".join(states), "}")
    print("Alphabet: {", " ".join(alphabet), "}")
    print("Initial State:", states[0])

    compute_new_final_states()
    compute_new_transitions()


# Main
if __name__ == "__main__":
    read_nfa()
    display_automaton()
