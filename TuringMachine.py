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
        self._line = []
        self.pointer = 0

    @property
    def line(self):
        i = self._line[0]
        while i != '1' and self.pointer != 0:
            self._line.pop(0)
            self.pointer -= 1
            i = self._line[0]
        return ''.join(self._line), self.pointer

    def step(self):
        step = self.configuration.get(f'{self.state} {self._line[self.pointer]}', -1)
        if step == -1:
            return
        self._line[self.pointer] = step['out_cell']
        self.pointer += letter2move[step['move']]
        self.state = step['out_state']

        if self.pointer == len(self._line):
            self._line.append('0')

        if self.pointer < 0:
            self._line = ['0'] + self._line
            self.pointer = 0

    def execute(self, word, initial_point=0, existing__line=False):
        if not existing__line:
            self._line = []

        counter = 0
        self.pointer = len(self._line) + initial_point
        self._line += list(word)
        self.state = 'q1'

        while True and self.step() != -1:
            counter += 1

            if self.state == 'q0':
                break

            if counter >= 50:
                return -1

