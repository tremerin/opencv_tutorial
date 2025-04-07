import cv2
import numpy as np

cap = cv2.VideoCapture("./resources/downloads/test_video.mp4")

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=blue_mask)

    cv2.imshow("frame", result)
    cv2.imshow("mask", blue_mask)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

"""
El modelo HSV (Hue, Saturation, Value, en español: Matiz, Saturación, Valor) es un 
sistema de representación de colores alternativo al clásico RGB (Rojo, Verde, Azul).
Se usa ampliamente en gráficos por computadora, diseño y procesamiento de imágenes
porque es más intuitivo para los humanos al describir colores en términos más naturales.

Componentes del modelo HSV:
H (Hue - Matiz)
    Representa el tipo de color (como rojo, azul, verde, etc.).
    Se mide en grados (0° a 360°) en una rueda de colores:
    0° o 360°: Rojo
    120°: Verde
    240°: Azul
    Los demás colores están entre estos valores (ej.: 60° es amarillo, 300° es magenta).
S (Saturation - Saturación)
    Indica la intensidad o pureza del color.
    Rango: 0% a 100% (o 0 a 1 en algunos sistemas).
    0%: Color gris (sin saturación).
    100%: Color totalmente vivo y puro.
V (Value - Valor o Brillo)
    Define el brillo del color.
    Rango: 0% a 100% (o 0 a 1).
    0%: Negro (sin brillo).
    100%: Color en su máxima luminosidad.

Ejemplos:
Rojo intenso: HSV(0°, 100%, 100%)
Rosa pastel: HSV(0°, 50%, 100%) (mismo matiz que el rojo, pero menos saturado).
Gris oscuro: HSV(0°, 0%, 50%) (sin matiz ni saturación, solo brillo intermedio).
"""
