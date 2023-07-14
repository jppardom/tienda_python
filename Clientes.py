from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Conexion import Conexion

class Clientes:
    def __init__(self, ventana):
        self.ventanaClientes = Toplevel(ventana)
        self.ventanaClientes.geometry('1100x650+12+12')
        self.ventanaClientes.focus_set()
        self.ventanaClientes.grab_set()
        self.ventanaClientes.transient(master=ventana)
        #Frame contenido
        self.frameContenido = LabelFrame(self.ventanaClientes, text="DETALLE DE CLIENTES")
        self.frameContenido.config(font=('Comic Sans MS', 12))
        self.frameContenido.grid(column=0, row=0, padx=3, pady=3, columnspan=4)

        #Cédula
        self.lblCedula = Label(self.frameContenido, text="Cédula:")
        self.lblCedula.config(font=('Comic Sans MS', 12))
        self.lblCedula.grid(column=0, row=1, padx=3, pady=3)
        self.txtCedula = Entry(self.frameContenido)
        self.txtCedula.config(font=('Comic Sans MS', 12))
        self.txtCedula.grid(column=1, row=1, padx=3, pady=3, columnspan=4)

        #Nombres
        self.lblNombres = Label(self.frameContenido, text="Nombres:")
        self.lblNombres.config(font=('Comic Sans MS', 12))
        self.lblNombres.grid(column=0, row=2, padx=3, pady=3)
        self.txtNombres = Entry(self.frameContenido)
        self.txtNombres.config(font=('Comic Sans MS', 12))
        self.txtNombres.grid(column=1, row=2, padx=3, pady=3)

        #Apellidos
        self.lblApellidos = Label(self.frameContenido, text="Apellidos:")
        self.lblApellidos.config(font=('Comic Sans MS', 12))
        self.lblApellidos.grid(column=2, row=2, padx=3, pady=3)
        self.txtApellidos = Entry(self.frameContenido)
        self.txtApellidos.config(font=('Comic Sans MS', 12))
        self.txtApellidos.grid(column=3, row=2, padx=3, pady=3)

        #Genero
        self.lblGenero = Label(self.frameContenido, text="Genero:")
        self.lblGenero.config(font=('Comic Sans MS', 12))
        self.lblGenero.grid(column=0, row=3, padx=3, pady=3)
        self.cbxGenero = ttk.Combobox (self.frameContenido)
        self.cbxGenero.config(font=('Comic Sans MS', 12))
        self.cbxGenero["values"] = "[Seleccione]", "Masculino", "Femenino"	
        self.cbxGenero.grid(column=1, row=3, padx=3, pady=3)

        #Direción
        self.lblDireccion = Label(self.frameContenido, text="Dirección:")
        self.lblDireccion.config(font=('Comic Sans MS', 12))
        self.lblDireccion.grid(column=2, row=3, padx=3, pady=3)
        self.txtDireccion = Entry(self.frameContenido)
        self.txtDireccion.config(font=('Comic Sans MS', 12))
        self.txtDireccion.grid(column=3, row=3, padx=3, pady=3)

        #Correo
        self.lblCorreo = Label(self.frameContenido, text="Correo:")
        self.lblCorreo.config(font=('Comic Sans MS', 12))
        self.lblCorreo.grid(column=0, row=4, padx=3, pady=3)
        self.txtCorreo = Entry(self.frameContenido)
        self.txtCorreo.config(font=('Comic Sans MS', 12))
        self.txtCorreo.grid(column=1, row=4, padx=3, pady=3)

        #Teléfono
        self.lblTelefono = Label(self.frameContenido, text="Teléfono:")
        self.lblTelefono.config(font=('Comic Sans MS', 12))
        self.lblTelefono.grid(column=2, row=4, padx=3, pady=3)
        self.txtTelefono = Entry(self.frameContenido)
        self.txtTelefono.config(font=('Comic Sans MS', 12))
        self.txtTelefono.grid(column=3, row=4, padx=3, pady=3)

        #Frame botones
        self.frameBotones = LabelFrame(self.ventanaClientes, text="FUNCIONALIDAD")
        self.frameBotones.config(font=('Comic Sans MS', 12))
        self.frameBotones.grid(column=4, row=0, padx=3, pady=3,)

        #Botones
        self.btnNuevo = Button(self.frameBotones, text="Nuevo", command=lambda:Clientes.debloquer_guardar(self))
        self.btnNuevo.config(font=('Comic Sans MS', 12))
        self.btnNuevo.grid(column=4,row=0, padx=3, pady=3, sticky=N+S+W+E)

        self.btnGuardar = Button(self.frameBotones, text="Guardar", command=lambda:Clientes.guardar(self))
        self.btnGuardar.config(font=('Comic Sans MS', 12))
        self.btnGuardar.grid(column=4,row=1, padx=3, pady=3, sticky=N+S+W+E)

        self.btnActualizar = Button(self.frameBotones, text="Actualizar")
        self.btnActualizar.config(font=('Comic Sans MS', 12))
        self.btnActualizar.grid(column=4,row=2, padx=3, pady=3, sticky=N+S+W+E)

        self.btnCancelar = Button(self.frameBotones, text="Cancelar", command=lambda:Clientes.bloquear(self))
        self.btnCancelar.config(font=('Comic Sans MS', 12))
        self.btnCancelar.grid(column=4,row=3, padx=3, pady=3, sticky=N+S+W+E)

        #Contenedor de tabla
        self.frameDatos = LabelFrame(self.ventanaClientes, text="DATOS DEL CLIENTE")
        self.frameDatos.config(font=('Comic Sans MS', 12))
        self.frameDatos.grid(column=0, row=4, padx=3, pady=3,columnspan=8)

        #popup nenu
        self.popup = Menu(self.ventanaClientes, tearoff=0)
        self.popup.add_command(label="EDITAR", command=lambda:Clientes.editar(self))
        self.popup.add_command(label="ELIMINAR")

        def do_popup(event):
            # display the popup menu
            try:
                self.popup.tk_popup(event.x_root, event.y_root, 0)
            finally:
                # make sure to release the grab (Tk 8.0a1 only)
                self.popup.grab_release()


        #Tabla para cargar clintes 
        self.data = ttk.Treeview(self.frameDatos, height=10, columns=('id', 'cedula', 'nombres', 'apellidos', 'genero', 'direccion', 'correo', 'telefono'), show="headings")
        self.data.grid(column=0, row=4, padx=3, pady=3, columnspan=8)
        self.data.heading("id", text = 'ID', anchor = CENTER)
        self.data.column("id", width=40)
        self.data.heading("cedula", text = 'CÉDULA', anchor = CENTER)
        self.data.column("cedula", width=70)
        self.data.heading("nombres", text = 'NOMBRE', anchor = CENTER)
        self.data.column("nombres", width=150)
        self.data.heading("apellidos", text = 'APELLIDOS', anchor = CENTER)
        self.data.column("apellidos", width=150)
        self.data.heading("genero", text = 'GENERO', anchor = CENTER)
        self.data.column("genero", width=80)
        self.data.heading("direccion", text = 'DIRECCIÓN', anchor = CENTER)
        self.data.column("direccion", width=200)
        self.data.heading("correo", text = 'CORREO', anchor = CENTER)
        self.data.column("correo", width=200)
        self.data.heading("telefono", text = 'TELÉFONO', anchor = CENTER)
        self.data.column("telefono", width=80)
        self.data.bind("<Button-3>", do_popup)
        Clientes.cargar(self)
        Clientes.bloquear(self)

    #Función para bloquer widget
    def bloquear(self):
        self.txtCedula.config(state='disabled')
        self.txtNombres.config(state='disabled')
        self.txtApellidos.config(state='disabled')
        self.cbxGenero['state'] = 'disabled'
        self.txtDireccion.config(state='disabled')
        self.txtCorreo.config(state='disabled')
        self.txtTelefono.config(state='disabled')
        self.btnGuardar.config(state='disabled')
        self.btnActualizar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnNuevo.config(state='normal')
    
    #Funicion para desbloquear para guardar datos 
    def debloquer_guardar(self):
        self.txtCedula.config(state='normal')
        self.txtNombres.config(state='normal')
        self.txtApellidos.config(state='normal')
        self.cbxGenero['state'] = 'normal'
        self.txtDireccion.config(state='normal')
        self.txtCorreo.config(state='normal')
        self.txtTelefono.config(state='normal')
        self.btnGuardar.config(state='normal')
        self.btnActualizar.config(state='disabled')
        self.btnCancelar.config(state='normal')
        self.btnNuevo.config(state='disabled')

    #Función para guardar datos de clientes
    def guardar (self):
        if self.txtCedula.get()!="" and self.txtNombres.get()!="" and self.txtApellidos.get()!="" and self.txtDireccion.get()!="" and self.txtTelefono.get()!="" and self.txtCorreo.get()!="":
           self.sql = 'INSERT INTO clientes (cedula, nombres, apellidos, genero, direccion, correo, telefono) VALUES (?,?,?,?,?,?,?)'
           self.parametros = (self.txtCedula.get(), self.txtNombres.get(), self.txtApellidos.get(), self.cbxGenero.get(), self.txtDireccion.get(), self.txtCorreo.get(), self.txtTelefono.get())
           if Conexion.run_query(self.sql, self.parametros):
               messagebox.showinfo(message="Datos del cliente guardados con éxito", title='Cientes')
               Clientes.cargar(self)
               Clientes.limpiar(self)
           else:
               messagebox.showerror(message='Los datos del cliente no se pueden guardar', title="cliente")
        else:
            messagebox.showwarning(message='El formularo posee campos obligatorios', title='Mensaje')

    #Fución para cargar datos de clientes
    def cargar (self):
        self.limpiar_tabla = self.data.get_children()
        for elemento in self.limpiar_tabla:
            self.data.delete(elemento)
        self.sql = "SELECT * FROM clientes"
        self.lista_tabla = Conexion.run_query(self.sql)
        for  row in self.lista_tabla:
            self.data.insert('', row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    #Función para limpiar el formulario
    def limpiar (self):
        self.txtCedula.delete(0, 'end')
        self.txtNombres.delete(0, 'end')
        self.txtApellidos.delete(0, 'end')
        self.cbxGenero.delete(0, 'end')
        self.txtDireccion.delete(0, 'end')
        self.txtCorreo.delete(0, 'end')
        self.txtTelefono.delete(0, 'end')
        self.txtCedula.focus()
        Clientes.bloquear(self)

    #Funicion para desbloquear para actualizar datos 
    def debloquer_actualizar(self):
        self.txtCedula.config(state='normal')
        self.txtNombres.config(state='normal')
        self.txtApellidos.config(state='normal')
        self.cbxGenero['state'] = 'normal'
        self.txtDireccion.config(state='normal')
        self.txtCorreo.config(state='normal')
        self.txtTelefono.config(state='normal')
        self.btnGuardar.config(state='disabled')
        self.btnActualizar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnNuevo.config(state='disabled')

    #Función para cargar los datos a los widget
    def editar (self):
        Clientes.debloquer_actualizar(self)

