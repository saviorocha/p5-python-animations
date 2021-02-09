from p5 import *

class Branch:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    
    def show():
        stroke(255)
        line(self.begin.x, self.end.y, self.end.x, self.begin.y)

    def create_branches():
        right = Branch()