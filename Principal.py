from tkinter import *
from Clientes import Clientes
from Productos import Productos

class Principal:
    def __init__(self):
        self.ventanaPrincipal = Tk()
        self.ventanaPrincipal.title("Sistemas de Facturación")
        m = self.ventanaPrincipal.maxsize()
        self.ventanaPrincipal.geometry('{}x{}+0+0'.format(*m))

        self.barraMenu = Menu(self.ventanaPrincipal)
        self.ventanaPrincipal.config(menu=self.barraMenu)

        self.menuAchivo = Menu(self.barraMenu, tearoff=0)
        self.menuAchivo.add_command(label='Información')
        self.menuAchivo.add_command(label='Salir', command=lambda:self.ventanaPrincipal.destroy())
        
        self.menuAdministracion = Menu (self.barraMenu, tearoff=0)
        self.menuAdministracion.add_command(label='Clientes', command=lambda:Clientes.__init__(self,self.ventanaPrincipal))
        self.menuAdministracion.add_command(label='Producotos', command=lambda:Productos.__init__(self,self.ventanaPrincipal))

        self.barraMenu.add_cascade(label="Archivo", menu=self.menuAchivo)
        self.barraMenu.add_cascade(label='Adminstación', menu=self.menuAdministracion)
        

        