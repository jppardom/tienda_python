from tkinter import *
from hashlib import sha1
from Conexion import Conexion
from tkinter import messagebox
class Usuarios:
    def __init__(self):   
        self.ventanaUsuarios = Tk()
        self.ventanaUsuarios.eval('tk::PlaceWindow . center')
        self.ventanaUsuarios.title("Ingreso de nuevos usuarios")
        #Contenedor
        self.frame = LabelFrame (self.ventanaUsuarios, text="Digite datos del usuario")
        self.frame.config(font=('Comic Sans MS', 20))
        self.frame.pack()

        #Cédula
        self.lblCedula = Label(self.frame, text="Cedula:")
        self.lblCedula.config(font=('Comic Sans MS', 18))
        self.lblCedula.grid(column=0, row=0, padx=10,pady=10, columnspan=2)

        self.txtCedula = Entry(self.frame)
        self.txtCedula.config(font=('Comic Sans MS', 18))
        self.txtCedula.grid(column=1, row=0, padx=10, pady=10, columnspan=4)

        #Nombres
        self.lblNombre = Label(self.frame, text="Nombres:")
        self.lblNombre.config(font=('Comic Sans MS', 18))
        self.lblNombre.grid(column=0, row=1, padx=10,pady=10, sticky="W")

        self.txtNombre = Entry(self.frame)
        self.txtNombre.config(font=('Comic Sans MS', 18))
        self.txtNombre.grid(column=1, row=1, padx=10, pady=10)

        #Apellidos
        self.lblApellidos = Label(self.frame, text="Apellidos:")
        self.lblApellidos.config(font=('Comic Sans MS', 18))
        self.lblApellidos.grid(column=2, row=1, padx=10,pady=10, sticky="W")

        self.txtApellidos = Entry(self.frame)
        self.txtApellidos.config(font=('Comic Sans MS', 18))
        self.txtApellidos.grid(column=3, row=1, padx=10, pady=10)

        #Correo
        self.lblCorreo = Label(self.frame, text="Correo:")
        self.lblCorreo.config(font=('Comic Sans MS', 18))
        self.lblCorreo.grid(column=0, row=2, padx=10,pady=10, sticky="W")

        self.txtCorreo = Entry(self.frame)
        self.txtCorreo.config(font=('Comic Sans MS', 18))
        self.txtCorreo.grid(column=1, row=2, padx=10, pady=10)

        #Username
        self.lblUsername = Label(self.frame, text="Usuario:")
        self.lblUsername.config(font=('Comic Sans MS', 18))
        self.lblUsername.grid(column=2, row=2, padx=10,pady=10, sticky="W")

        self.txtUsername = Entry(self.frame)
        self.txtUsername.config(font=('Comic Sans MS', 18))
        self.txtUsername.grid(column=3, row=2, padx=10, pady=10)

        #contraseña
        self.lblContraseña = Label(self.frame, text="Contraseña:")
        self.lblContraseña.config(font=('Comic Sans MS', 18))
        self.lblContraseña.grid(column=0, row=3, padx=10,pady=10, sticky="W")

        self.txtContraseña = Entry(self.frame)
        self.txtContraseña.config(show="*", font=('Comic Sans MS', 18))
        self.txtContraseña.grid(column=1, row=3, padx=10, pady=10)

         #Repetir contraseña
        self.lblRepetirContraseña = Label(self.frame, text="Repetir:")
        self.lblRepetirContraseña.config(font=('Comic Sans MS', 18))
        self.lblRepetirContraseña.grid(column=2, row=3, padx=10,pady=10, sticky="W")

        self.txtRepetirContraseña = Entry(self.frame)
        self.txtRepetirContraseña.config(show="*", font=('Comic Sans MS', 18))
        self.txtRepetirContraseña.grid(column=3, row=3, padx=10, pady=10)

        #Botornes

        self.btnGuardar = Button(self.frame, text="Guardar", command=lambda:Usuarios.guardarUsuario(self))
        self.btnGuardar.config(font=('Comic Sans MS', 18))
        self.btnGuardar.grid(column=0, row=4, padx=10, pady=10, columnspan=3)

        self.btnVolver = Button(self.frame, text="Salir", command=lambda:Usuarios.salir(self))
        self.btnVolver.config(font=('Comic Sans MS', 18))
        self.btnVolver.grid(column=1, row=4, padx=10, pady=10, columnspan=4)
        self.ventanaUsuarios.mainloop()

    def salir(self):
        self.ventanaUsuarios.destroy()

    def guardarUsuario (self):
        if self.txtContraseña.get() == self.txtRepetirContraseña.get():
            self.sql = "INSERT INTO usuarios (cedula, nombre, apellido, correo, username, password) VALUES (?,?,?,?,?,?)"
            has= sha1(self.txtContraseña.get().encode('utf-8')).hexdigest()
            self.parametros = (self.txtCedula.get(), self.txtNombre.get(), self.txtApellidos.get(), self.txtCorreo.get(), self.txtUsername.get(),has)
            if Conexion.run_query(self.sql, self.parametros):
                messagebox.showinfo(message="Datos guardaados correctamente", title="Guardar datos")
                self.ventanaUsuarios.destroy()
            else:
                messagebox.showwarning(message="No se pueden guarde datos", title="Error al guardar datos")
                self.ventanaUsuarios.destroy()
        else:
            messagebox.showinfo(message="La contraseñas no son iguales", title="Validar contraseña")
            self.txtRepetirContraseña.delete(0,'end')
            self.txtContraseña.delete(0,'end')