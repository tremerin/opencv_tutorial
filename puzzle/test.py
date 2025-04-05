import cv2
import sys
import tkinter as tk
from PIL import Image, ImageTk

# Leer argumento: tamaño de fragmento
if len(sys.argv) == 2 and sys.argv[1].isnumeric():
    size = int(sys.argv[1])
else:
    print("Uso: python puzzle.py <tamaño_de_pieza>")
    exit()

# Inicializar ventana y leer imagen
window = tk.Tk()
img = cv2.imread("../resources/poligons.jpg") 
rows = img.shape[0] // size
cols = img.shape[1] // size

# Convertir imagen a RGB (PIL usa RGB, OpenCV usa BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Lista para guardar imágenes y labels
pieces = []
labels = []
grid_positions = {}  # Diccionario para rastrear posiciones ocupadas

# Crear fragmentos y almacenarlos
for y in range(rows):
    for x in range(cols):
        crop = img[y*size:(y+1)*size, x*size:(x+1)*size]
        img_pil = Image.fromarray(crop)
        img_tk = ImageTk.PhotoImage(img_pil)
        pieces.append(img_tk)

# Variables para el arrastre
drag_data = {"widget": None, "row": 0, "col": 0, "x": 0, "y": 0}

# Funciones de arrastrar y soltar
def on_drag_start(event):
    widget = event.widget
    drag_data["widget"] = widget
    drag_data["row"] = widget.grid_info()["row"]
    drag_data["col"] = widget.grid_info()["column"]
    drag_data["x"] = event.x
    drag_data["y"] = event.y
    widget.lift()  # Eleva el widget para que parezca que se está arrastrando

def on_drag_motion(event):
    widget = drag_data["widget"]
    if widget:
        # Mueve el widget con el cursor
        x = event.x_root - window.winfo_rootx() - drag_data["x"]
        y = event.y_root - window.winfo_rooty() - drag_data["y"]
        widget.place(x=x, y=y)

def on_drop(event):
    widget = drag_data["widget"]
    if not widget:
        return
    
    # Calcular en qué casilla se soltó
    x = event.x_root - window.winfo_rootx()
    y = event.y_root - window.winfo_rooty()
    
    # Determinar la fila y columna donde se soltó
    col = x // size
    row = y // size
    
    # Asegurarse de que está dentro de los límites
    col = max(0, min(col, cols-1))
    row = max(0, min(row, rows-1))
    
    # Mover la pieza a la nueva posición
    widget.grid(row=row, column=col)
    widget.place_forget()  # Quitar el posicionamiento absoluto
    
    drag_data["widget"] = None

# Crear etiquetas con imágenes y enlazar eventos
i = 0
for y in range(rows): 
    for x in range(cols):
        lbl = tk.Label(window, image=pieces[i], bd=2, relief="raised")
        lbl.grid(row=y, column=x)
        lbl.bind("<Button-1>", on_drag_start)
        lbl.bind("<B1-Motion>", on_drag_motion)
        lbl.bind("<ButtonRelease-1>", on_drop)
        labels.append(lbl)
        i += 1

window.mainloop()