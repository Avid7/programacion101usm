import numpy as np 
import cv2 
x0=0
y0=0
xf=0        #coordenadas tanto iniciales como finales del centro del rectangulo
yf=0
cap = cv2.VideoCapture('xdfinal.mp4') #Lee y abre el video seleccionado

ret,frame = cap.read()#cap.read=lee el primer frame.
#ret=verdadero(si hay un frame), falso si no lo hay-
#frame=imagen en si

r,h,c,w = 150,100,600,150# Coordenadas Rectangulo 
track_window = (c,r,w,h)#Lo que dibuja el rectangulo 
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
flag = True    
tiempo = 0 #Contador de frames 
while(1):
    ret ,frame = cap.read() #Por cada iteracion, lee un frame.
    if ret == True: #si hay un frame, se ejecuta todo
        hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((90.,30.,30.)), np.array((160.,255.,255.)))
        #asigna el rango de valores(colores) a buscar
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])#Histograma
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)#Rango a seguir para estabilizarlo
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#transforma el color 
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)#backproj
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)
        cv2.imshow('mask',mask)
        if flag:
            x0=x
            y0=y
        if (c, r)!=(x, y):
            tiempo+=1
            flag = False
        k = cv2.waitKey(1) & 0xff #Tecla
        if k == 27: #tecla de escape
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)#Ultimo frame del video 
    else:  #Si no hay frame, todo se corta
        break 
xf=x
yf=y
if tiempo!=0:
    print (x0, y0)
    print (xf, yf)
    print ((x0-xf)**2 +(y0-yf)**2)**0.5
    tiempo=tiempo/30.0
    print tiempo
    print ((x0-xf)**2 +(y0-yf)**2)**0.5/tiempo
cv2.destroyAllWindows()
cap.release()
