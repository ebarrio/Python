from tkinter import *
from tkinter import messagebox
import pandas as pd
from pandas import DataFrame

class Sesion:
    def __init__(self,user,password):
        self.user = user
        self.password = password

        self.loaded = False

        self.num_acounts = 0
        self.num_likes = 10
        self.num_follows = 10
        self.num_unfollows = 10

        self.acounts = []
    def new_data_base(self):
        print('Create csv file')
    def save_data_base(self):
        print('Save data in csv')
    def load_data_base(self):
        self.loaded = True
        read = pd.read_csv(self.user + '.csv')
        read_dict = read.to_dict()
        contraseña_sesion = read_dict.get('Sespass')
        self.num_acounts = len(contraseña_sesion)
        if (contraseña_sesion[0] == self.password):
            print('Correct pass')
            self.cuentas = read_dict.get('Cuenta')
            self.contraseñas = read_dict.get('Contraseña')
            self.hastags = read_dict.get('Hastags')

        to_write = {
            'Cuenta' : self.cuentas,
            'Constraseña' : self.contraseñas,
            'Hastags' : self.hastags
        }
        df = DataFrame(to_write)
        df.to_csv('saved.csv', index = False)
if __name__ == '__main__':
    user_season = Sesion('Eladio', 'Barrio')
    user_season.load_data_base()

#NUEVA SESIÓN
def frame_com_nueva_sesion():
    
    ns_raiz = Tk()
    ns_raiz.title("Nueva sesión")
    ns_frame = Frame(ns_raiz)
    ns_frame.pack()

    Label(ns_frame, text = 'Nombre de la nueva sesión:').grid(sticky = 'W', row = 1, column = 1)
    Label(ns_frame, text = 'Contraseña de la nueva sesión:').grid(sticky = 'W', row = 2, column = 1)

    user_sesion = StringVar()
    pass_sesion = StringVar()
    user_entry = Entry(ns_frame, textvariable = user_sesion)
    user_entry.grid(sticky = 'W', row = 1, column = 2)
    pass_entry = Entry(ns_frame, textvariable = pass_sesion)
    pass_entry.grid(sticky = 'W', row = 2, column = 2)

    Label(ns_frame, text = '      ').grid(row = 1, column = 3)

    def com_crear_sesion():
        user = user_entry.get()
        passw = pass_entry.get()
        print('Usuario:' + user + '\n' + 'Contraseña:' + passw)
        ns_raiz.destroy()

    Button(ns_frame,width = 10, text = "Crear sesión", command = com_crear_sesion).grid(sticky = 'W', row = 1, column = 4)

    def com_cancelar():
        ns_raiz.destroy()

    Button(ns_frame,width = 10, text = "Cancelar", command = com_cancelar).grid(sticky = 'W', row = 2, column = 4)


    ns_raiz.mainloop()


#CARGAR SESIÓN
def frame_com_cargar_sesion():
    cs_raiz = Tk()
    cs_raiz.title("Cargar sesión")
    cs_frame = Frame(cs_raiz)
    cs_frame.pack()
    Label(cs_frame, text = 'Nombre de la sesión:').grid(sticky = 'W', row = 1, column = 1)
    Label(cs_frame, text = 'Contraseña de la sesión:').grid(sticky = 'W', row = 2, column = 1)

    user_sesion = StringVar()
    pass_sesion = StringVar()
    user_entry = Entry(cs_frame, textvariable = user_sesion)
    user_entry.grid(sticky = 'W', row = 1, column = 2)
    pass_entry = Entry(cs_frame, textvariable = pass_sesion)
    pass_entry.grid(sticky = 'W', row = 2, column = 2)

    user = ' '
    passw = ' '
    def com_cargar_sesion():
        user = user_entry.get()
        passw = pass_entry.get()
        fin_cargar_sesion(user, passw)
        cs_raiz.destroy()
        """
    def fin_cargar_sesion(user , passw):
        out = Sesion(user, passw)
        """

    def com_cancelar():
        cs_raiz.destroy()

    Label(cs_frame, text = '      ').grid(row = 1, column = 3)
    Button(cs_frame, width = 10, text = "Cargar sesión", command = com_cargar_sesion).grid(sticky = 'W', row = 1, column = 4)
    Button(cs_frame, width = 10, text = "Cancelar", command = com_cancelar).grid(sticky = 'W', row = 2, column = 4)


#GUARDAR SESIÓN
def frame_com_guardar_sesion():
    messagebox.showinfo('Guardar sesión','Se ha guardado la sesión')

#GUARDAR SESIÓN COMO
def frame_com_guardar_sesion_como():
    messagebox.showinfo('Guardar sesión','Se ha guardado la sesión')
    

