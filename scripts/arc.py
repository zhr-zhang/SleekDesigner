from stripe import Stripe

class arc(Stripe):
    def __init__(self,center,a,b,body_color,outline_color):
        super.__init__(body_color,outline_color)
        self.x0, self.y0=center
        self.x1, self.y1=a
        self.x2, self.y2=b

    def distance2(self,x,y):
        pass