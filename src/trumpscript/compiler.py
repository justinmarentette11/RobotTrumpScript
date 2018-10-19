# Compiler for TrumpScript
# 1/17/2016

from ast import *

from src.trumpscript.parser import *
from src.trumpscript.tokenizer import *

class Compiler:

    def __init__(self):
        self.tk = Tokenizer()
        self.prs = Parser()

    def compile(self, source, flip_flopping, setter):

        if compiled.get(source, None) is None:
            modu = self.parse(self.tokenize(source, flip_flopping))
            fix_missing_locations(modu)
            print("compiling " + source)
            compiled[source] = compile(modu, filename="<ast>", mode="exec")
            print(compiled)
            setter(compiled)
        exec(compiled[source])

    def parse(self, tokens):
        return self.prs.parse(tokens)

    def tokenize(self, filename, flip_flopping):
        return self.tk.tokenize(filename, flip_flopping)
