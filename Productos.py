from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Conexion import Conexion

class Productos:
    def __init__(self, ventana):
        self.ventanaProductos = Toplevel(ventana)
        self.ventanaProductos.geometry('1100x650+12+12')
        self.ventanaProductos.focus_set()
        self.ventanaProductos.grab_set()
        self.ventanaProductos.transient(master=ventana)
        #Frame contenido
        self.frameContenido = LabelFrame(self.ventanaProductos, text="DETALLE DE PRODUCTOS")
        self.frameContenido.config(font=('Comic Sans MS', 12))
        self.frameContenido.grid(column=0, row=0, padx=3, pady=3, columnspan=4)

        #Nombre del Producto
        self.lblNombre = Label(self.frameContenido, text="Nombre:")
        self.lblNombre.config(font=('Comic Sans MS', 12))
        self.lblNombre.grid(column=0, row=1, padx=3, pady=3)
        self.txtNombre = Entry(self.frameContenido)
        self.txtNombre.config(font=('Comic Sans MS', 12))
        self.txtNombre.grid(column=1, row=1, padx=3, pady=3, columnspan=4)

        #Precio
        self.lblPrecio = Label(self.frameContenido, text="Precio:")
        self.lblPrecio.config(font=('Comic Sans MS', 12))
        self.lblPrecio.grid(column=0, row=2, padx=3, pady=3)
        self.txtPrecio = Entry(self.frameContenido)
        self.txtPrecio.config(font=('Comic Sans MS', 12))
        self.txtPrecio.grid(column=1, row=2, padx=3, pady=3)

        #Stock
        self.lblStock = Label(self.frameContenido, text="Stock:")
        self.lblStock.config(font=('Comic Sans MS', 12))
        self.lblStock.grid(column=2, row=2, padx=3, pady=3)
        self.txtStock = Entry(self.frameContenido)
        self.txtStock.config(font=('Comic Sans MS', 12))
        self.txtStock.grid(column=3, row=2, padx=3, pady=3)

        #Frame botones
        self.frameBotones = LabelFrame(self.ventanaProductos, text="FUNCIONALIDAD")
        self.frameBotones.config(font=('Comic Sans MS', 12))
        self.frameBotones.grid(column=4, row=0, padx=3, pady=3,)

        #Botones
        self.btnNuevo = Button(self.frameBotones, text="Nuevo", command=lambda:Productos.debloquer_guardar(self))
        self.btnNuevo.config(font=('Comic Sans MS', 12))
        self.btnNuevo.grid(column=4,row=0, padx=3, pady=3, sticky=N+S+W+E)

        self.btnGuardar = Button(self.frameBotones, text="Guardar")
        self.btnGuardar.config(font=('Comic Sans MS', 12))
        self.btnGuardar.grid(column=4,row=1, padx=3, pady=3, sticky=N+S+W+E)

        self.btnActualizar = Button(self.frameBotones, text="Actualizar")
        self.btnActualizar.config(font=('Comic Sans MS', 12))
        self.btnActualizar.grid(column=4,row=2, padx=3, pady=3, sticky=N+S+W+E)

        self.btnCancelar = Button(self.frameBotones, text="Cancelar", command=lambda:Productos.limpiar(self))
        self.btnCancelar.config(font=('Comic Sans MS', 12))
        self.btnCancelar.grid(column=4,row=3, padx=3, pady=3, sticky=N+S+W+E)

        #Contenedor de tabla
        self.frameDatos = LabelFrame(self.ventanaProductos, text="DATOS DE LOS PRODUCTOS")
        self.frameDatos.config(font=('Comic Sans MS', 12))
        self.frameDatos.grid(column=0, row=4, padx=3, pady=3,columnspan=8)

        #popup nenu
        self.popup = Menu(self.ventanaProductos, tearoff=0)
        self.popup.add_command(label="EDITAR")
        self.popup.add_command(label="ELIMINAR")

        def do_popup(event):
            # display the popup menu
            try:
                self.popup.tk_popup(event.x_root, event.y_root, 0)
            finally:
                # make sure to release the grab (Tk 8.0a1 only)
                self.popup.grab_release()


        #Tabla para cargar clintes 
        self.data = ttk.Treeview(self.frameDatos, height=10, columns=('id', 'nombre', 'precio', 'stock'), show="headings")
        self.data.grid(column=0, row=4, padx=3, pady=3, columnspan=4)
        self.data.heading("id", text = 'ID', anchor = CENTER)
        self.data.column("id", width=40)
        self.data.heading("nombre", text = 'NOMBRE PRODUCTO', anchor = CENTER)
        self.data.column("nombre", width=150)
        self.data.heading("precio", text = 'PRECIO', anchor = CENTER)
        self.data.column("precio", width=70)
        self.data.heading("stock", text = 'STOCK', anchor = CENTER)
        self.data.column("stock", width=80)
        self.data.bind("<Button-3>", do_popup)
        Productos.limpiar(self)

    #Función para bloquer widget
    def bloquear(self):
        self.txtNombre.config(state='disabled')
        self.txtPrecio.config(state='disabled')
        self.txtStock.config(state='disabled')
        self.btnGuardar.config(state='disabled')
        self.btnActualizar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnNuevo.config(state='normal')
    
    #Funicion para desbloquear para guardar datos 
    def debloquer_guardar(self):
        self.txtNombre.config(state='normal')
        self.txtPrecio.config(state='normal')
        self.txtStock.config(state='normal')
        self.btnGuardar.config(state='normal')
        self.btnActualizar.config(state='disabled')
        self.btnCancelar.config(state='normal')
        self.btnNuevo.config(state='disabled')

     #Función para limpiar el formulario
    
    #Función para limpiar el formulario
    def limpiar (self):
        self.txtNombre.delete(0, 'end')
        self.txtPrecio.delete(0, 'end')
        self.txtStock.delete(0, 'end')
        self.txtNombre.focus()
        Productos.bloquear(self)