import cv2
import numpy as np

from util import image_resize


def preprocesamiento (imagen):
    # leer las matrices de calibracion
    cam_matrix = np.genfromtxt("./calibration/cam_matrix.txt",delimiter=",")
    coef_dist = np.genfromtxt ("./calibration/coef_dist.txt",delimiter=",")
    
    ################################
    # calibracion 
    ################################
    h,  w = imagen.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(cam_matrix,coef_dist , (w,h), 0, (w,h))
    # undistort
    dst = cv2.undistort(imagen, cam_matrix, coef_dist, None, newcameramtx)
    # crop the image
    x, y, w, h = roi
    calibrated = dst[y:y+h, x:x+w]
    ################################
    # Modificaion de tamaño
    ################################
    resized = image_resize(calibrated,height=480)
    ################################
    # reduccion a escala de grises
    ################################
    grises = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    return grises,resized

