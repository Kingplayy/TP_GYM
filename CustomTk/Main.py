import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Login:
    def __init__(self):
        # Ventana principal
        self.root = ctk.CTk()
        self.root.geometry("400x300")
        self.root.title("Sistema Energym")
        self.Crear_botones()
        
    def validar_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        # Leer usuarios desde el archivo de texto
        with open("Usuarios.txt", "r") as archivo:
            usuarios = archivo.readlines()
            
        for usuario in usuarios:
            datos = usuario.strip().split(";")
            if datos[0] == username and datos[1] == password:
                self.label_resultado.configure(text=f"Login exitoso! Bienvenido {username}.", text_color="green")
                self.abrir_toplevel()
                return
            else:
                self.label_resultado.configure(text="Usuario o contraseña incorrectos.", text_color="red")
            
    def Crear_botones(self):
        # Campo de usuario
        label_username = ctk.CTkLabel(master=self.root, text="Usuario:")
        label_username.pack(pady=10)
        self.entry_username = ctk.CTkEntry(master=self.root)
        self.entry_username.pack(pady=5)

        # Campo de contraseña
        label_password = ctk.CTkLabel(master=self.root, text="Contraseña:")
        label_password.pack(pady=10)
        self.entry_password = ctk.CTkEntry(master=self.root, show="*")
        self.entry_password.pack(pady=5)

        # Botón de login
        boton_login = ctk.CTkButton(master=self.root, text="Iniciar Sesión", command=self.validar_login)
        boton_login.pack(pady=20)

        # Resultado del login
        self.label_resultado = ctk.CTkLabel(master=self.root, text="")
        self.label_resultado.pack(pady=10)
        
    def abrir_toplevel(self):
        toplevel = ctk.CTkToplevel(self.root)
        toplevel.geometry("300x200")
        toplevel.title("Ventana Principal")

        # Puedes agregar widgets a esta nueva ventana
        etiqueta_bienvenida = ctk.CTkLabel(toplevel, text="Bienvenido a la aplicación")
        etiqueta_bienvenida.pack(pady=20)
    
root = Login()
root.root.mainloop()