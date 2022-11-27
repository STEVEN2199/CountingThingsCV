import cv2

#LEER LA IMAGEN A USAR
imagen = cv2.imread('monedas.jpg')

#TRABAJO SOBRE EL CLON DE MI IMAGEN
clon = imagen.copy()

#TRANSFORMA LA IMAGEN A ESCALA DE GRISES 
grises = cv2.cvtColor(clon, cv2.COLOR_BGR2GRAY)
_,th =  cv2.threshold(grises, 240, 255, cv2.THRESH_BINARY_INV)

#Para OpenCV 3
#_,cnts,_ = cv2.findContours(th, cv2.RETR_EXTERNAL,
#	cv2.CHAIN_APPROX_SIMPLE)

#Para OpenCV 4
cnts,_ = cv2.findContours(th, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

#DIBUJA LOS CONTRONOS SOBRE MI IMAGEN
cv2.drawContours(imagen, cnts, -1, (255,0,0),2)
print('Contornos: ', len(cnts))

#ME PERMITE PONER TEXTO SOBRE UNA IMAGEN
font = cv2.FONT_HERSHEY_SIMPLEX
i=0
for c in cnts:
    #Podemos encontrar el centro de la mancha usando momentos en OpenCV.
	M=cv2.moments(c)
	if (M["m00"]==0): M["m00"]=1
	x=int(M["m10"]/M["m00"])
	y=int(M['m01']/M['m00'])

	mensaje = 'Objeto#:' + str(i+1)
	#ME PERMITE PONER TEXTO SOBRE UNA IMAGEN
	cv2.putText(clon,mensaje,(x-40,y),font,0.75,
		(255,0,0),2,cv2.LINE_AA)
	#DIBUJA LOS CONTRONOS SOBRE MI IMAGEN
	cv2.drawContours(clon, [c], 0, (255,0,0),2)
	cv2.imshow('Imagen', clon)
	cv2.waitKey(0)
	i = i+1
cv2.destroyAllWindows()