from model.algorithms import DDA
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap

if __name__=='__main__':
    x = int(input('Ingrese x1:'))
    y = int(input('Ingrese y1:'))
    
    x2 = int(input('Ingrese x2:'))
    y2 = int(input('Ingrese y2:'))

    obj = DDA(x,y,x2,y2)

    (x_vars,y_vars)=obj.print_chart()

    # graficando el resultado del algoritmo
    output_file('grafica.html')
    fig= figure()
    mapper = linear_cmap(field_name='y', palette=Spectral6 ,low=min(y_vars) ,high=max(y_vars))
    fig.square(x_vars,y_vars,color=mapper)
    show(fig)
