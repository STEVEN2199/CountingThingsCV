import cv2

from mostrarResultados import mostrarResultados
from preprocesamiento import preprocesamiento
from segmentacion import segmentacion

#input
imagen = cv2.imread('./images/prueba2.jpeg')

# Modulo 1
grises, calibrated = preprocesamiento(imagen) 
# Modulo 2
cnts = segmentacion (grises)
# Modulo 3
mostrarResultados(calibrated,cnts)            
