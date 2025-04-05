import cv2
import sys
import tkinter as tk
from PIL import Image, ImageTk



if len(sys.argv) == 2 and sys.argv[1].isnumeric():
    size = int(sys.argv[1])
else:
    exit()


window = tk.Tk()
img = cv2.imread("../resources/poligons.jpg")
rows = int(img.shape[0]/size)
columns = int(img.shape[1]/size)
print(f"image size:{img.shape[0]} x {img.shape[1]}\nparts size: {size}")
print(f"rows: {rows}, columns: {columns}")

"""imgs = list()
for y in range(rows):
    for x in range(columns):
        tag = img[y*size : y*size + size, x*size : x*size + size]
        #conversion
        tag = cv2.cvtColor(tag, cv2.COLOR_BGR2RGB)
        tag = Image.fromarray(tag)
        tag = ImageTk.PhotoImage(image=tag)
        imgs.append(tag)"""

imgs = [ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(img[y*size : y*size + size, x*size : x*size + size], cv2.COLOR_BGR2RGB))) for y in range(rows) for x in range(columns)]
lbl_parts = [tk.Label(window, image=imgs[i]).grid(row=int(i/columns),column=i-int(i/columns)*columns) for i in range(len(imgs))]

def mouse_pos(event):
    #print(f"winfo {window.winfo_rooty()}, {window.winfo_rootx()}") #ventana en la pantalla
    #print(f"mouse event{event.y}, {event.x}") #mouse en elemento
    x = (event.x_root - window.winfo_rootx()) // size
    y = (event.y_root - window.winfo_rooty()) // size
    print(f"mouse event root{y}, {x}") #mouse en la ventana
    widget = event.widget
    print(widget.grid_info()["row"], widget.grid_info()["column"])
window.bind("<Motion>", mouse_pos)

window.mainloop()
