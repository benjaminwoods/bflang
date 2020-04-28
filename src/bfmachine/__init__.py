"""
.. module:: bfmachine
    :platform: Unix, Windows
    :synopsis: Brainf**k machine.
"""

import sys
from io import BytesIO

class BFMachine:
    def __init__(self,
                 malloc=lambda: list(0 for i in range(30000)),
                 stdin=sys.stdin,
                 stdout=sys.stdout):
        self.stdin = stdin
        self.stdout = stdout
        self.malloc = malloc
        self.__block = False
    def run(self, code=''):
        """
        Run!
        """
        
        # Memory pointer
        j = 0
        
        if isinstance(code, str):
            code = BytesIO(bytes(code, encoding='utf-8'))
        
        mem = self.malloc()
        code.seek(0)
        c = code.read(1)
        while c:
            # Reading code
            if c == b'>':
                j += 1
            elif c == b'<':
                j -= 1
            elif c == b'+':
                mem[j] += 1
            elif c == b'-':
                mem[j] -= 1
            elif c == b'.':
                print(chr(mem[j]),
                      file=self.stdout, end='')
            elif c == b',':
                if self.stdin is None:
                    mem[j] = ord(input())
                else:
                    mem[j] = self.stdin.read(1)
            elif c == b'[':
                if mem[j] == 0:
                    c = code.read(1)
                    _scope = 0
                    while not(c == b']' and _scope == 0):
                        if c == b'[':
                            _scope += 1
                        elif c == b']':
                            _scope -= 1
                        c = code.read(1)
            elif c == b']':
                if mem[j] != 0:
                    code.seek(-2, 1)
                    c = code.read(1)
                    _scope = 0
                    while not(c == b'[' and _scope == 0):
                        if c == b'[':
                            _scope += 1
                        elif c == b']':
                            _scope -= 1
                        code.seek(-2, 1)
                        c = code.read(1)
            else:
                pass
            
            if j < 0:
                raise MemoryError('Negative pointer.')
            elif mem[j] < 0:
                raise MemoryError('Negative byte.')
            
            c = code.read(1)