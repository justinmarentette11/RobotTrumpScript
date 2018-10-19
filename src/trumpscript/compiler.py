# Compiler for TrumpScript
# 1/17/2016

from ast import *

from src.trumpscript.parser import *
from src.trumpscript.tokenizer import *

class Compiler:

    def __init__(self, flip_flopping):
        self.tk = Tokenizer()
        self.prs = Parser()
        self.flip_flopping = flip_flopping

    def compile(self, source, compiled):
        if compiled.get(source, None) is None:
            modu = self.parse(self.tokenize(source))
            fix_missing_locations(modu)
            print("compiling " + source)
            compiled[source] = compile(modu, filename="<ast>", mode="exec")
            print(compiled)
        exec(compiled[source])

    def parse(self, tokens):
        return self.prs.parse(tokens)

    def tokenize(self, filename):
        return self.tk.tokenize(filename, self.flip_flopping)
