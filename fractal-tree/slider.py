from p5 import *

class Slider:
    def __init__(self,low,high,default):
        '''slider has range from low to high
        and is set to default'''
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False
        
    def position(self,x,y):
        '''slider's position on screen'''
        self.x = x
        self.y = y
        #the position of the rect you slide:
        self.rectx = self.x + mapping(self.val, self.low, self.high, 0, 120)
        self.recty = self.y - 10
        
    def value(self):
        '''updates the slider and returns value'''
        #gray line behind slider
        
        stroke_weight(4)
        stroke(200)
        line((self.x,self.y), (self.x + 120,self.y))
        
        #press mouse to move slider
        if mouse_is_pressed and dist((mouse_x,mouse_y), (self.rectx,self.recty)) < 20:
            self.rectx = mouse_x
        
        #constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + 120)
        
        #draw rectangle
        stroke_weight(1)
        stroke(0)
        fill(255)
        rect((self.rectx, self.recty), 10, 20)
        self.val = mapping(self.rectx,self.x,self.x + 120,self.low,self.high)
        
        #draw label
        # fill(0)
        # text_size(12)
        # text(int(self.val),self.rectx,self.recty + 35)
        return self.val

def mapping(n, start1, stop1, start2, stop2):
    """Set the background color for the p5.renderer.

    :param args: 
    :param args:
    :param args: 
    :param args: 
    :param args: 
    :returns: """
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2
