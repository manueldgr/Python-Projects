import numpy as np
from matplotlib import pyplot as plt
import tkinter

"""
En este código es para crear una regresión lineal obteniendo los datos del usuario.
"""
def gui():
    pass

def data_user():
    """se tomaran los datos que ingrese el usuario"""

    data_n = "\nIngrese la cantidad de datos: "
    var0 = int(input(data_n))
    cont0 = 1
    cont1 = 1
    var_list1 = []
    var_list2 = []
    while cont0 <= var0:
        data_x = "Digite el valor de x: "
        data_y = "Digite el valor de y: "
        var1 = float(input(data_x))
        var2 = float(input(data_y))
        var_list1.append(var1)
        var_list2.append(var2)
        cont0 += 1
    vector_x = np.array(var_list1)
    vector_y = np.array(var_list2)
    print(f"\nVector x -> {vector_x}")
    print(f"Vector y -> {vector_y}")
    return vector_x, vector_y, var0

def calculo(x,y,n):
    """en esta función se hacen todos los calculos necesarios para la regresión."""

    sum_mult = np.sum(x*y)
    sum_exp_2 = np.sum(x**2)
    sum_x = np.sum(x); sum_y = np.sum(y)
    prom_x = (1/n)*sum_x; prom_y = (1/n)*sum_y
    pendiente = ((n*sum_mult) - (sum_x*sum_y))/((n*sum_exp_2) - ((sum_x)**2)) #a1
    print(f"pendiente (m)->\t{pendiente}")
    intersc = prom_y - (pendiente*prom_x) #a0
    print(f"intersección (b)->\t{intersc}")
    print(f"regresión lineal->\t{pendiente:.4f}x + {intersc:.4f}")
    return pendiente, intersc

vec_x, vec_y,var0 = data_user()
pendiente, intersc = calculo(vec_x,vec_y,var0)

def graph(ax_x,ax_y,m,inter,ndata):
    space = np.linspace(min(ax_x),max(ax_x),num=100)
    vector_linealeq = []
    for i in space:
        f_x = m*(i) + inter
        vector_linealeq.append(f_x)
    eq_lineal = np.array(vector_linealeq)
    plt.plot(space,eq_lineal,linestyle='--',label='Ecuación Lineal')
    plt.plot(ax_x,ax_y,'o',label='Data')
    plt.xlabel('x'),plt.ylabel('y')
    plt.title('REGRESIÓN LINEAL')
    plt.legend()
    plt.grid(True)
    plt.show()

graph(vec_x,vec_y,pendiente,intersc,var0)
