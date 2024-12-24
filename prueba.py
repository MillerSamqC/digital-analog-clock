import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Reloj Digital")
        
        # Configurar el tamaño y posición de la ventana
        self.root.geometry("400x200")
        self.root.configure(bg='black')
        
        # Crear la etiqueta para mostrar el tiempo
        self.label = tk.Label(
            self.root,
            font=('digital-7', 80),
            background='black',
            foreground='#aacde2'
        )
        self.label.pack(anchor='center', pady=20)
        
        # Iniciar la actualización del tiempo
        self.update_time()
    
    def update_time(self):
        """Actualiza la hora cada segundo"""
        # Obtener la hora actual en formato HH:MM:SS
        string_time = strftime('%H:%M:%S')
        
        # Actualizar el texto de la etiqueta
        self.label.config(text=string_time)
        
        # Programar la próxima actualización en 1000ms (1 segundo)
        self.label.after(1000, self.update_time)
    
    def run(self):
        """Inicia el bucle principal de la aplicación"""
        self.root.mainloop()

if __name__ == '__main__':
    # Crear y ejecutar el reloj
    clock = DigitalClock()
    clock.run()