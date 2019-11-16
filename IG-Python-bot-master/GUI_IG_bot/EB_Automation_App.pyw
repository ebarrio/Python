# NOT FINISHED
from tkinter import *
from tkinter import messagebox
from frame import *
class Season:
        def __init__(self,user,password):
                self.user = user
                self.password = password
                self.run_likes = False
                self.run_follows = False
                self.run_unfollows = False
        
        
        def print(self):
                print('Run likes:' + str(self.run_likes))
                print('Run follows:' + str(self.run_follows))
                print('Run unfollows:' + str(self.run_unfollows))

user_season = Season("eladio", "barrio")
# Generamos la ventana
root = Tk()

#Cambiamos nombre de la ventana
root.title("Eladio application")

#Bloqueamos el cambio de tamaño de la ventana
root.resizable(True,True)

#Cambiamos color del fondo
#root.config(bg="white", width = 300, height = 300)


# Configuración barra de menu superior
barra_menu = Menu(root)
root.config(menu=barra_menu)

# Opción Archivo
archivo_menu_1 = Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Archivo", menu=archivo_menu_1)
#Subopciones de Archivo
archivo_menu_1.add_command(label = "Nueva sesión", command = frame_com_nueva_sesion)

def launch_frame_com_cargar_sesion():
        #user_season = frame_com_cargar_sesion()
        pass

archivo_menu_1.add_command(label = "Cargar sesión", command = launch_frame_com_cargar_sesion)
archivo_menu_1.add_command(label = "Guardar sesión", command = frame_com_guardar_sesion)
archivo_menu_1.add_command(label = "Guardar sesión como...", command = frame_com_guardar_sesion_como)
#Añadimos linea separacion
archivo_menu_1.add_separator()
archivo_menu_1.add_command(label = "Cerrar")

def com_salir():
    valor_seleccionado = messagebox.askquestion('Salir','¿Quieres salir del programa?')
    if(valor_seleccionado == 'yes'):
        root.destroy()
archivo_menu_1.add_command(label = "Salir", command = com_salir)

# Opción Edición
archivo_menu_2 = Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Edición", menu=archivo_menu_2)
archivo_menu_2.add_command(label = "Deshacer")
archivo_menu_2.add_command(label = "Rehacer")
#Añadimos linea separacion
archivo_menu_2.add_separator()
archivo_menu_2.add_command(label = "Copiar")
archivo_menu_2.add_command(label = "Cortar")
archivo_menu_2.add_command(label = "Pegar")


# Opción Herramientas
archivo_menu_3 = Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Herramientas", menu=archivo_menu_3)
archivo_menu_3.add_command(label = "Ocultar/Mostrar herramientas")

# Opción Ayudas
#Función para mostrar ventana emergente de Acerca de...
def com_licencia():
    messagebox.showwarning('Información de la licencia','Producto bajo licencia EJEMPLO')
archivo_menu_4 = Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Ayudas", menu=archivo_menu_4)
archivo_menu_4.add_cascade(label = "Licencia", command = com_licencia)

#Función para mostrar ventana emergente de Acerca de...
def com_acerca_de():
    messagebox.showinfo('Información adicional','Informacion de ejemplo')
archivo_menu_4.add_cascade(label = "Acerca de...", command = com_acerca_de)


#CONFIGURACIÓN DE LA SESIÓN DE INSTAGRAM:
frame = Frame(root)
frame.pack()
frame4_banda = Frame(root)
frame4_banda.pack()
frame2 = Frame(root)
frame2.pack()
"""
frame.config(bg = "black")
frame.config(width = "300", height = "300")
"""

logo_programa = PhotoImage(file = "logoebq.png")

Label(frame, image = logo_programa).grid(row = 1, column = 1)
Label(frame, text = "EBQ Automation Product", font = 50).grid(row = 1, column = 2)
Label(frame, text = '       ').grid(row = 1, column = 4)
Label(frame, text = '       ').grid(row = 6, column = 4)
Label(frame, text="Elige acciones a realizar en las cuentas de Instagram:").grid(row = 2, column = 2)
#Selección configuración de la sesion de Instagram
checked_follow = IntVar()
checked_unfollow = IntVar()
checked_like = IntVar()

def com_check_insta_op():
        if(checked_follow.get() == 1):
                user_season.run_follows = True
        else:
                user_season.run_follows = False

        if(checked_unfollow.get() == 1):
                user_season.run_unfollows = True
        else:
                user_season.run_unfollows = False

        if(checked_like.get() == 1):
                user_season.run_likes = True
        else:
                user_season.run_likes = False
                
Checkbutton(frame, text = "Follow", variable = checked_follow, onvalue = 1, offvalue = 0, command = com_check_insta_op).grid(sticky = 'W', row = 4, column = 2)
Checkbutton(frame, text = "Unfollow", variable = checked_unfollow, onvalue = 1, offvalue = 0, command = com_check_insta_op).grid(sticky = 'W', row = 5, column = 2)
Checkbutton(frame, text = "Like", variable = checked_like, onvalue = 1, offvalue = 0, command = com_check_insta_op).grid(sticky = 'W', row = 3, column = 2)

#Boton ejecutrar sesión
def com_ejecutrar_sesion():
        user_season.print()
Button(frame, text = "Ejecutar sesión", command = com_ejecutrar_sesion).grid(row = 4, column = 3)

#Barra negra decorativa
Label(frame4_banda, bg = 'black', text= '                                                                                                                            ').pack()
#Frame de mostrar valores
Label(frame2, text = 'Numero de cuentas:').grid(row=1, column = 1)
Entry(frame2).grid(row=1, column = 2)

Label(frame2, text = 'Numero de likes:').grid(row=2, column = 1)
Entry(frame2).grid(row=2, column = 2)

Label(frame2, text = 'Numero de follows:').grid(row=3, column = 1)
Entry(frame2).grid(row=3, column = 2)

Label(frame2, text = 'Numero de unfollows:').grid(row=4, column = 1)
Entry(frame2).grid(row=4, column = 2)

frame3 = Frame(root)
frame3.pack()
Label(frame3, text = 'Inicia sesión para modificar parametros').grid(row=1, column = 1)
#Bucle de la ventana (Despues de la inicialización)
root.mainloop()
