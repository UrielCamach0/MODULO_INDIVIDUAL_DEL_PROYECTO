import tkinter as tk
from tkinter import messagebox, ttk

class App:
    """
    Clase principal que define la interfaz grafica de la aplicacion TEC HUB.
    """

    def __init__(self, root):
        """
        Constructor de la clase App. Inicializa la ventana principal, el contenedor de login 
        y los elementos iniciales de la interfaz.
        """
        self.root = root
        self.root.title("TEC HUB - CONTROL DE ACTIVIDADES")
        self.root.geometry("800x600")
        self.root.config(bg="#f0f0f0")

        # Contenedor para el formulario de login
        self.login_frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Elementos del formulario de login
        tk.Label(self.login_frame, text="INICIAR SESION", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        self.username = tk.Entry(self.login_frame, width=30, font=("Arial", 12))
        self.username.insert(0, "USUARIO")  # Texto por defecto
        self.username.pack(pady=5)

        self.email = tk.Entry(self.login_frame, width=30, font=("Arial", 12))
        self.email.insert(0, "CORREO")  # Texto por defecto
        self.email.pack(pady=5)

        self.password = tk.Entry(self.login_frame, width=30, show="*", font=("Arial", 12))
        self.password.insert(0, "CONTRASENA")  # Texto por defecto
        self.password.pack(pady=5)

        # Boton para iniciar sesion
        tk.Button(self.login_frame, text="ACCEDER", bg="#080843", fg="white", font=("Arial", 12, "bold"),
                  command=self.login).pack(pady=15)

        # Contenedor para la interfaz principal (invisible al inicio)
        self.main_frame = tk.Frame(self.root, bg="white")

        # Barra lateral para el menu
        self.sidebar = tk.Frame(self.main_frame, bg="#080843", width=200, height=600)
        self.sidebar.pack(side="left", fill="y")

        # Contenedor principal para las secciones
        self.content = tk.Frame(self.main_frame, bg="white")
        self.content.pack(side="right", expand=True, fill="both")

        # Menu lateral con botones para navegar entre secciones
        self.menu_buttons = [
            ("INICIO", lambda: self.show_section("inicio")),
            ("PERFIL", lambda: self.show_section("perfil")),
            ("TAREAS", lambda: self.show_section("tareas")),
            ("SALIR", self.logout)
        ]

        for text, command in self.menu_buttons:
            # Agrega botones al menu lateral
            tk.Button(self.sidebar, text=text, bg="#080843", fg="white", font=("Arial", 12), command=command,
                      anchor="w", padx=10, relief="flat").pack(fill="x")

        # Diccionario para gestionar las diferentes secciones
        self.sections = {
            "inicio": self.create_inicio_section(),
            "perfil": self.create_perfil_section(),
            "tareas": self.create_tareas_section()
        }

    def login(self):
        """
        Metodo para manejar el inicio de sesion.
        Verifica que todos los campos esten llenos antes de permitir el acceso.
        """
        if self.username.get() and self.email.get() and self.password.get():
            # Si los campos estan llenos, destruye el formulario de login y muestra la interfaz principal
            self.login_frame.destroy()
            self.main_frame.pack(fill="both", expand=True)
        else:
            # Muestra una advertencia si hay campos vacios
            messagebox.showwarning("Advertencia", "Por favor llena todos los campos.")

    def logout(self):
        """
        Metodo para cerrar sesion.
        Oculta la interfaz principal y reinicia el formulario de login.
        """
        self.main_frame.pack_forget()
        self.__init__(self.root)  # Reinicia la aplicacion

    def show_section(self, section_name):
        """
        Metodo para mostrar una seccion especifica de la aplicacion.
        Desoculta la seccion seleccionada y oculta las demas.
        
        :param section_name: Nombre de la seccion a mostrar (inicio, perfil, tareas).
        """
        for section in self.sections.values():
            section.pack_forget()  # Oculta todas las secciones
        self.sections[section_name].pack(fill="both", expand=True)  # Muestra la seccion seleccionada

    def create_inicio_section(self):
        """
        Crea y devuelve el contenedor de la seccion 'Inicio'.
        """
        frame = tk.Frame(self.content, bg="white")
        tk.Label(frame, text="BIENVENIDO DE VUELTA", font=("Arial", 16, "bold"), bg="white").pack(pady=20)
        tk.Label(frame, text="TEC HUB", font=("Arial", 14), bg="white").pack()
        return frame

    def create_perfil_section(self):
        """
        Crea y devuelve el contenedor de la seccion 'Perfil'.
        """
        frame = tk.Frame(self.content, bg="white")
        tk.Label(frame, text="PERFIL", font=("Arial", 16, "bold"), bg="white").pack(pady=20)
        tk.Label(frame, text="Aqui se muestra toda la informacion del estudiante.", font=("Arial", 12), bg="white").pack()
        return frame

    def create_tareas_section(self):
        """
        Crea y devuelve el contenedor de la seccion 'Tareas', que incluye una tabla con informacion de tareas.
        """
        frame = tk.Frame(self.content, bg="white")
        tk.Label(frame, text="TAREAS", font=("Arial", 16, "bold"), bg="white").pack(pady=20)

        # Definicion de columnas para la tabla
        columns = ("Proyecto", "Fecha Limite", "Estado")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        tree.heading("Proyecto", text="NOMBRE DEL PROYECTO")
        tree.heading("Fecha Limite", text="FECHA LIMITE")
        tree.heading("Estado", text="ESTADO")

        # Datos de ejemplo para las tareas
        tareas = [
            ("PROYECTO 1", "2024-11-04", "COMPLETADA"),
            ("PROYECTO 2", "2024-12-01", "EN PROGRESO"),
            ("PROYECTO 3", "2025-01-10", "PENDIENTE")
        ]
        for tarea in tareas:
            tree.insert("", "end", values=tarea)  # Agrega las tareas a la tabla

        tree.pack(fill="both", expand=True)
        return frame
