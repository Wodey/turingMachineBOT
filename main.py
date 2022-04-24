from TuringMachine import TuringMachine

inp = ['q1 0 q1 0 R', 'q1 1 q2 0 R', 'q2 1 q1 0 R', 'q2 0 q0 1 S']

tm = TuringMachine(inp)

word = '1110'
if (c := tm.execute(word)) == -1:
    print(f'Слово {word} невыполнимо')

print(tm.line)

word = '110111'

print(tm.execute(word, 4) == -1)

print(tm.line)