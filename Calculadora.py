from tkinter import *
from tkinter import messagebox
from math import *

ventana = Tk()
ventana.title('CALCULADORA')
#ventana.iconbitmap('Mio.ico')
ventana.config(bg = 'gray15')
ventana.resizable(0,0)
ventana.geometry('320x400')
#320x365


#Entrada
cuadro = Entry(ventana, font=('calibri 20'),fg='white', justify='right',relief='flat')
cuadro.place(x=10, y=10, width=300 , height=60)
cuadro.config(bg = 'gray15')

#Indice
i=0

#Funciones

def ingreso_datos(a):
    global i
    cuadro.insert(i,a)
    i=i+1

def borrar ():
    cuadro.delete(0,END)
    i=0

def limpiar_num():
    display_state = cuadro.get()
    if len(display_state):
        nueva_pantalla = display_state[:-1]
        borrar()
        cuadro.insert(0,nueva_pantalla)
    else:
        borrar()


def calculo():
	global i

	ecuacion = cuadro.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			cuadro.delete(0,END)
			cuadro.insert(0,result)
			longitud = len(result)
			i = longitud

		except:
			result = 'ERROR'
			cuadro.delete(0,END)
			cuadro.insert(0,result)
	else:
		pass

def  autor():
    msg = messagebox.showinfo(message='DARWIN TICS',title='Autor')
    

#Primera Fila de Botones ------------------------------------------
#Boton 1 -----C Borara todo ------------ya esta
boton_C = Button(ventana, text='CE',font=('calibri 15'),fg='white',command=lambda: borrar())
boton_C.place(x=10, y=80, width=75 , height=55)
boton_C.config(bg = 'gray13')

#Boton 2 -----% Procentaje
boton_porc = Button(ventana, text='EXP',font=('calibri 15'),fg='white',command=lambda:ingreso_datos('**'))
boton_porc.place(x=87, y=80, width=75 , height=55)
boton_porc.config(bg = 'gray13')

#Boton 3 -----⌫ Borrar cada numero
boton_P = Button(ventana, text='⌫',font=('calibri 15'),fg='white',command=lambda:limpiar_num())
boton_P.place(x=164, y=80, width=75 , height=55)
boton_P.config(bg = 'gray13')

#Boton 4 -----(÷) Dividir ---------ya esta

bot_dividir  = Button(ventana, text='÷',font=('calibri 15'),fg='white',command=lambda: ingreso_datos('/'))
bot_dividir.place(x=241, y=80, width=70 , height=55)
bot_dividir.config(bg = 'gray13')

#Segunda Fila -------------------------------------

#Boton 1 --- (7)
boton_7 = Button(ventana, text='7',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(7))
boton_7.place(x=10, y=135, width=75 , height=55)
boton_7.config(bg = 'gray5')


#Boton 2 --- (8)
boton_8 = Button(ventana, text='8',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(8))
boton_8.place(x=87, y=135, width=75 , height=55)
boton_8.config(bg = 'gray5')

#Boton 3 --- (9)
boton_9 = Button(ventana, text='9',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(9))
boton_9.place(x=164, y=135, width=75 , height=55)
boton_9.config(bg = 'gray5')

#Boton 4 ---(x)
boton_x = Button(ventana, text='x',font=('calibri 15'),fg='white',command=lambda: ingreso_datos('*'))
boton_x.place(x=241, y=135, width=70 , height=55)
boton_x.config(bg = 'gray13')

#Tercera Fila -----------------------
#Boton 1 ---(4)
boton_4 = Button(ventana, text='4',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(4))
boton_4.place(x=10, y=190, width=75 , height=55)
boton_4.config(bg = 'gray5')

#Boton 2  ---(5)
boton_5 = Button(ventana, text='5',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(5))
boton_5.place(x=87, y=190, width=75 , height=55)
boton_5.config(bg = 'gray5')

#Boton 3 ---(6)
boton_6 = Button(ventana, text='6',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(6))
boton_6.place(x=164, y=190, width=75 , height=55)
boton_6.config(bg = 'gray5')

#Boton 4 ---(-)
bot_restar = Button(ventana, text='-',font=('calibri 15'),fg='white',command=lambda: ingreso_datos('-'))
bot_restar .place(x=241, y=190, width=70 , height=55)
bot_restar .config(bg = 'gray13')

#Cuarta Fila ------------------------------------

#Boton 1 ---(1)
boton_1 = Button(ventana, text='1',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(1))
boton_1.place(x=10, y=245, width=75 , height=55)
boton_1.config(bg = 'gray5')

#Boton 2 ---(2)
boton_2 = Button(ventana, text='2',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(2))
boton_2.place(x=87, y=245, width=75 , height=55)
boton_2.config(bg = 'gray5')

#Boton 3 ---(3)
boton_3 = Button(ventana, text='3',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(3))
boton_3.place(x=164, y=245, width=75 , height=55)
boton_3.config(bg = 'gray5')

#Boton 4 ---(+)
bot_suma = Button(ventana, text='+',font=('calibri 15'),fg='white',command=lambda: ingreso_datos('+'))
bot_suma.place(x=241, y=245, width=70 , height=55)
bot_suma.config(bg = 'gray13')

#Quinto Fila 

#Boton 1 ---(0)
boton_0 = Button(ventana, text='0',font=('calibri 15'),fg='white',command=lambda: ingreso_datos(0))
boton_0.place(x=10, y=300, width=150 , height=55)
boton_0.config(bg = 'gray13')

#Boton 2 ---(.)
bot_punto = Button(ventana, text='.',font=('calibri 15'),fg='white',command=lambda: ingreso_datos('.'))
bot_punto.place(x=164, y=300, width=75 , height=55)
bot_punto.config(bg = 'gray13')

#Boton 3 ---(=) salida 
bot_salida = Button(ventana, text='=',font=('calibri' ,20),fg='white',activebackground="DeepSkyBlue2", bg ='#999AB8',command=lambda: calculo())
bot_salida.place(x=241, y=300, width=70 , height=55)
bot_salida.config(bg = 'gray13')
#SteelBlue3

#Sexta Fila 

#Boton 1 ---(user)

boton_u = Button(ventana, text='Autor',font=('Comic sens MC',12,'bold'),fg='white', command=autor)
boton_u.place(x=164, y=354, width=147 , height=45)
boton_u.config(bg = 'gray13')

#etiqueta 1
nombrelk =Label(ventana, text='CALCULADORA',font=('Comic sens MC',15,'bold'))
nombrelk.place(x=10, y=357, width=147 , height=19)#38
nombrelk.config(bg = 'gray15')
nombrelk.config(fg='Royalblue1', justify='right')

#etiqueta 2
nombrelk =Label(ventana, text='BASICA',font=('Comic sens MC',13))
nombrelk.place(x=10, y=377, width=147 , height=19)#38
nombrelk.config(bg = 'gray15')
nombrelk.config(fg='gray99', justify='right')

ventana.mainloop()






























