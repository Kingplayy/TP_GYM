import customtkinter as ctk
from PIL import Image, ImageTk  # Importar librerías de PIL

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul

# Definir la clase principal de la aplicación
class Ventana_principal:
    def crear_ventana(self):
        self.Ventana = ctk.CTk()
        
        # Configurar la ventana principal
        self.Ventana.title("Image Example")
        self.Ventana.geometry("800x500")
        self.Ventana.resizable(False, False)

        # Configurar el grid layout
        self.Ventana.grid_columnconfigure(1, weight=1)
        self.Ventana.grid_rowconfigure(0, weight=1)

        # Llamar a los métodos para construir la interfaz
        self.create_left_frame()
        self.create_right_frame()
        self.Ventana.mainloop()

    def create_left_frame(self):
        # Crear el frame izquierdo (menú de navegación)
        self.frame_left = ctk.CTkFrame(self.Ventana, width=200)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        # Añadir un logo o título
        self.logo_label = ctk.CTkLabel(self.frame_left, text="Systema Energym", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)

        # Botones del menú
        self.home_button = ctk.CTkButton(self.frame_left, text="Inicio", command=self.home_button_action)
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        self.frame2_button = ctk.CTkButton(self.frame_left, text="Inscripciones", command=self.frame2_button_action)
        self.frame2_button.grid(row=2, column=0, padx=20, pady=10)

        self.frame3_button = ctk.CTkButton(self.frame_left, text="Perfil", command=self.frame3_button_action)
        self.frame3_button.grid(row=3, column=0, padx=20, pady=10)

        # Botón desplegable
        self.dropdown_button = ctk.CTkOptionMenu(self.frame_left, values=["System", "Dark", "Light"], command=self.change_theme)
        self.dropdown_button.grid(row=4, column=0, padx=20, pady=10, sticky="s")

        # Botón de Salir
        self.exit_button = ctk.CTkButton(self.frame_left, text="Salir", command=self.quit_app, fg_color="red", hover_color="dark red")
        self.exit_button.grid(row=5, column=0, padx=20, pady=20, sticky="s")

    def create_right_frame(self):
    # Crear el frame derecho (área principal)
        frame = ctk.CTkFrame(self.Ventana, corner_radius=10)
        frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    # Cargar la imagen
        try:
            logo = Image.open("Imagenes/biceps.jpg")
            logo = logo.resize((200, 200), Image.Resampling.LANCZOS)  # Usa Image.ANTIALIAS si tienes una versión de Pillow antigua
            logo = ctk.CTkImage(light_image=logo, size=(200, 200))
            
            logo_label = ctk.CTkLabel(frame, image=logo, text="")
            logo_label.grid(row=0, column=0, padx=20, pady=10)
            
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        # Botones en el área central
        for i in range(4):
            button = ctk.CTkButton(frame, text=f"CTkButton {i+1}", command=lambda i=i: self.button_action(i))
            button.grid(row=i+1, column=0, padx=20, pady=10)

    # Métodos para manejar las acciones de los botones
    def home_button_action(self):
        print("Home button pressed")

    def frame2_button_action(self):
        print("Frame 2 button pressed")

    def frame3_button_action(self):
        print("Frame 3 button pressed")

    def button_action(self, button_number):
        print(f"CTkButton {button_number + 1} pressed")

    def change_theme(self, choice):
        ctk.set_appearance_mode(choice)
        print(f"Theme changed to {choice}")

    # Método para salir de la aplicación
    def quit_app(self):
        self.Ventana.quit()  # Cierra la aplicación
        print("App has been closed")