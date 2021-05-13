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


    def crd (self,start_point,finish_point, increment):
        list_of_points=[round(j) for j in range(start_point,finish_point,increment)]
        return list_of_points


    def print_chart(self):
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

       