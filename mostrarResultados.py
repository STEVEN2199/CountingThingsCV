import cv2

def mostrarResultados (imagen0,cnts):
    imagen = imagen0.copy()
    cv2.drawContours(imagen, cnts, -1, (255,0,0),2)
    print('Contornos: ', len(cnts))

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
        cv2.putText(imagen,mensaje,(x-40,y),font,0.75,
            (255,0,0),2,cv2.LINE_AA)
        #DIBUJA LOS CONTRONOS SOBRE MI IMAGEN
        cv2.drawContours(imagen, [c], 0, (255,0,0),2)
        cv2.imshow('Objetos', imagen)
        cv2.imshow('Imagen', imagen0)
        cv2.waitKey(0)
        i = i+1
    cv2.destroyAllWindows()
