letter2move = {
    'S': 0,
    'R': 1,
    "L": -1
}

class TuringMachine:
    def __init__(self, configuration):
        self.configuration = {}
        for i in configuration:
            in_state, in_cell, out_state, out_cell, move = i.split(' ')
            self.configuration[in_state +' ' + in_cell] = {
                'out_cell': out_cell,
                'move': move,
                'out_state': out_state
            }
        self.line = ['0']
        self.pointer = 0

    def step(self):
        step = self.configuration[f'{self.state} {self.line[self.pointer]}']
        self.line[self.pointer] = step['out_cell']
        self.pointer += letter2move[step['move']]
        self.state = step['out_state']

        if self.pointer == len(self.line):
            self.line.append('0')

        if self.pointer < 0:
            self.line = ['0'] + self.line
            self.pointer = 0

    def execute(self, word, initial_point=0):
        counter = 0
        self.pointer = len(self.line) + initial_point
        self.line += list(word)
        self.state = 'q1'

        while True:
            self.step()
            counter += 1

            if self.state == 'q0':
                break

            if counter >= 50:
                return -1

