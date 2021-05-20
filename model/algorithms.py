# class Points:
#     def __init__(self):
#         self.x=None
#         self.y=None
    
#     @property
#     def x(self):
#         return self.x
    
#     @x.setter
#     def x(self, x_point):
#         self.x = x_point

#     @property
#     def y(self):
#         return self.y
    
#     @y.setter
#     def y(self, y_point):
#         self.y = y_point

class DDA:
    # def __init__(self,point1,point2):
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2



    def print_chart(self):
        """Algoritmo DDA retorna 2 listas con los puntos cartecianos"""
        dx = abs(self.x2-self.x1)
        dy = abs(self.y2-self.y1)
        steps = 0
        if dx>dy:
            steps = dx
        else:
            steps = dy

        increment_x = dx / steps     
        increment_y = dy / steps

        p1 = self.x1
        p3 = self.y1
        x_vars=[p1]
        y_vars=[p3]
        for i in range(steps):
            p1 += increment_x
            n = round(p1)
            x_vars.append(n)

            p3 += increment_y
            n = round(p3)
            y_vars.append(n)
        return x_vars,y_vars

class Bresenham:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def print_chart(self):
        """Algoritmo Bresenham retorna 2 listas con los puntos cartecianos"""
        x = self.x1
        y = self.y1

        dx = abs(self.x2 -x)
        dy = abs(self.y2 -y)
        p = 2 * dy -dx
        x_vars=[]
        y_vars=[]
        while x <= self.x2:
            x_vars.append(x)
            y_vars.append(y)
            x += 1
            if p<0:
                p = p + 2 * dy
            else:
                p = p + (2 * dy) - (2 * dx)
                y += 1
        return x_vars,y_vars
