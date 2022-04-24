from TuringMachine import TuringMachine

inp = ['q1 0 q4 0 R', 'q1 1 q2 0 R', 'q2 0 q3 0 R', 'q2 1 q2 1 R', 'q3 0 q4 1 R', 'q3 1 q3 1 R', 'q4 0 q5 1 L',
       'q4 1 q7 0 R', 'q5 0 q6 0 L', 'q5 1 q5 1 L', 'q6 0 q1 0 R', 'q6 1 q6 1 L', 'q7 1 q8 0 R', 'q8 0 q8 0 S']

tm = TuringMachine(inp)

word = '1111111111111'

tm.execute(word)

print(tm.line)
