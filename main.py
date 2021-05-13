from model.algorithms import DDA
from bokeh.plotting import figure, output_file, show

if __name__=='__main__':
    x = int(input('Ingrese x1:'))
    y = int(input('Ingrese y1:'))
    
    x2 = int(input('Ingrese x2:'))
    y2 = int(input('Ingrese y2:'))

    obj = DDA(x,y,x2,y2)

    (x_vars,y_vars)=obj.print_chart()
