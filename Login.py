from tkinter import *
from Usuarios import Usuarios
from Conexion import Conexion
from tkinter import messagebox
from hashlib import sha1
from Principal import Principal
class Login:
    def __init__(self, login):
        self.ventanaLogin = login
        self.ventanaLogin.title("INICIO SESIÓN")

        #Contenedor
        self.frame = LabelFrame (self.ventanaLogin, text="TIENDA EN LINEA")
        self.frame.config(font=('Comic Sans MS', 20))
        self.frame.pack()

        #widget para el login
        self.lblUsername = Label(self.frame, text="Usuario:")
        self.lblUsername.config(font=('Comic Sans MS', 18))
        self.lblUsername.grid(column=0, row=0, padx=3,pady=3, sticky="W")

        self.txtUsername = Entry(self.frame)
        self.txtUsername.config(font=('Comic Sans MS', 18))
        self.txtUsername.grid(column=1, row=0, padx=3, pady=3)

        self.lblPassword = Label(self.frame, text="Contraseña:")
        self.lblPassword.config(font=('Comic Sans MS', 18))
        self.lblPassword.grid(column=0, row=1, padx=3,pady=3, sticky="W")

        self.txtPassword = Entry(self.frame)
        self.txtPassword.config(show="*", font=('Comic Sans MS', 18))
        self.txtPassword.grid(column=1, row=1, padx=3, pady=3)

        self.btnIngresar = Button (self.frame, text="Ingresar", command=self.loguear)
        self.btnIngresar.config(font=('Comic Sans MS', 18))
        self.btnIngresar.grid(column=0, row=2, padx=3, pady=3,columnspan=2)

        self.btnUsuarios = Button (self.frame, text="Registo de usuarios", command=self.crearUsuarios)
        self.btnUsuarios.config(font=('Comic Sans MS', 18))
        self.btnUsuarios.grid(column=0, row=3, padx=3, pady=3,columnspan=2)

    def crearUsuarios(self):
        self.ventanaLogin.destroy()
        Usuarios.__init__(self)
    
    def loguear (self):
        self.sql = 'SELECT * FROM usuarios WHERE username=? AND password=?'
        has= sha1(self.txtPassword.get().encode('utf-8')).hexdigest()
        self.parametros = (self.txtUsername.get(),has)
        data = Conexion.run_query(self.sql, self.parametros)
        if bool(data):
           messagebox.showinfo(message="Bienvenidos al sistema", title="Bienvenidos")
           self.ventanaLogin.destroy()
           Principal.__init__(self)
        else:
            messagebox.showwarning(message="Usuario o contraseña incorrecta", title="Error")
            pass
if __name__ == "__main__":
    login = Tk ()
    objLogin = Login(login)
    login.eval('tk::PlaceWindow . center')
    login.mainloop()