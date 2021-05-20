from bokeh.core.enums import SizingMode
from model.algorithms import DDA,Bresenham
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap



menu = """
        1)Bresenham

        2)DDA

        Ingresa una opción:
        --> """

if __name__=='__main__':
    print(menu,end=None)

    dato = int(input())
    x = int(input('Ingrese x1:'))
    y = int(input('Ingrese y1:'))
    
    x2 = int(input('Ingrese x2:'))
    y2 = int(input('Ingrese y2:'))

    if dato==1:
        obj = Bresenham(x,y,x2,y2)
    else:
        obj = DDA(x,y,x2,y2)

    (x_vars,y_vars)=obj.print_chart()

    # graficando el resultado del algoritmo
    output_file('grafica.html')
    fig= figure(title="DDA")
    fig.background_fill_color = "black"
    mapper = linear_cmap(field_name='y', palette=Spectral6 ,low=min(y_vars) ,high=max(y_vars))
    # efecto visual al centro
    for i in range(len(x_vars)):
        x_vars[i]+= 0.5
        y_vars[i]+=0.5
    fig.square(x_vars,y_vars,size= 98,color=mapper)
    show(fig)
