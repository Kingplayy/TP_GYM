import customtkinter as ctk
from PIL import Image, ImageTk  # Importar librerías de PIL

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul

# Definir la clase principal de la aplicación
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurar la ventana principal
        self.title("Image Example")
        self.geometry("800x500")

        # Configurar el grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Llamar a los métodos para construir la interfaz
        self.create_left_frame()
        self.create_right_frame()

    def create_left_frame(self):
        # Crear el frame izquierdo (menú de navegación)
        self.frame_left = ctk.CTkFrame(self, width=200)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        # Añadir un logo o título
        self.logo_label = ctk.CTkLabel(self.frame_left, text="Image Example", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)

        # Botones del menú
        self.home_button = ctk.CTkButton(self.frame_left, text="Home", command=self.home_button_action)
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        self.frame2_button = ctk.CTkButton(self.frame_left, text="Frame 2", command=self.frame2_button_action)
        self.frame2_button.grid(row=2, column=0, padx=20, pady=10)

        self.frame3_button = ctk.CTkButton(self.frame_left, text="Frame 3", command=self.frame3_button_action)
        self.frame3_button.grid(row=3, column=0, padx=20, pady=10)

        # Botón desplegable
        self.dropdown_button = ctk.CTkOptionMenu(self.frame_left, values=["System", "Dark", "Light"], command=self.change_theme)
        self.dropdown_button.grid(row=4, column=0, padx=20, pady=10, sticky="s")

        # Botón de Salir
        self.exit_button = ctk.CTkButton(self.frame_left, text="Salir", command=self.quit_app, fg_color="red", hover_color="dark red")
        self.exit_button.grid(row=5, column=0, padx=20, pady=20, sticky="s")

    def create_right_frame(self):
        # Crear el frame derecho (área principal)
        self.frame_right = ctk.CTkFrame(self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # Cargar y mostrar la imagen
        image = Image.open("ruta_de_tu_imagen.png")  # Cambia esto por la ruta de tu imagen
        image = image.resize((400, 150))  # Redimensionar la imagen al tamaño deseado
        self.image_tk = ImageTk.PhotoImage(image)  # Convertir la imagen a PhotoImage compatible con Tkinter

        # Etiqueta con imagen en el área central
        self.large_image_label = ctk.CTkLabel(self.frame_right, image=self.image_tk, text="")
        self.large_image_label.grid(row=0, column=0, padx=20, pady=20)

        # Botones en el área central (sin imágenes)
        for i in range(4):
            button = ctk.CTkButton(self.frame_right, text=f"CTkButton {i+1}", command=lambda i=i: self.button_action(i))
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
        self.quit()  # Cierra la aplicación
        print("App has been closed")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = App()  # Crear una instancia de la clase App
    app.mainloop()  # Ejecutar el bucle principal de la app
