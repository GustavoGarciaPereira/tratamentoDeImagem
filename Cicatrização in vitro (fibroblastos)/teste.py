import numpy as np
from cv2 import cv2 as cv
import os


arq = open("resultados.txt","w")
arq.write("Arquivo"+"\t"+"Brancos(não células)"+"\t"+"Pretos(células)"+"\t"+"Total"+"\t"+"%Branco"+"\t"+"%Preto"+"\n")

for imgArq in os.listdir():
    if(imgArq.endswith(".jpg")):
        print(imgArq)
        img = cv.imread(imgArq)

        #suavização
        blur = cv.blur(img,(5,5))
        #suavização gaussiana
        gaus = cv.GaussianBlur(img,(5,5),0)
        #mediana
        median = cv.medianBlur(img,5)
        #bilateral
        bilat = cv.bilateralFilter(img,9,75,75)

        imgCinza = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
        cv.imshow("Thresh1", imgCinza)



        for i in range(200, 255, 10):
            nomeArq = imgArq+'_threshold'+str(i)+'Blur.png'
            imgCinza = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
            ret,thresh = cv.threshold(imgCinza,i,255,cv.THRESH_BINARY)
            cv.imwrite(nomeArq,thresh)
            pretos = np.count_nonzero(thresh==0)
            brancos = np.count_nonzero(thresh==255)
            total = pretos+brancos
            percPretos = 100*pretos/total
            percBrancos = 100*brancos/total
            arq.write(nomeArq+"\t"+str(brancos)+"\t"+str(pretos)+"\t"+str(total)+"\t"+str(percBrancos).replace('.', ',')+"\t"+str(percPretos).replace('.', ',')+"\n")

            
            nomeArq = imgArq+'_threshold'+str(i)+'Gaus.png'
            imgCinza = cv.cvtColor(gaus, cv.COLOR_BGR2GRAY)
            ret,thresh = cv.threshold(imgCinza,i,255,cv.THRESH_BINARY)
            cv.imwrite(nomeArq,thresh)
            pretos = np.count_nonzero(thresh==0)
            brancos = np.count_nonzero(thresh==255)
            total = pretos+brancos
            percPretos = 100*pretos/total
            percBrancos = 100*brancos/total
            arq.write(nomeArq+"\t"+str(brancos)+"\t"+str(pretos)+"\t"+str(total)+"\t"+str(percBrancos).replace('.', ',')+"\t"+str(percPretos).replace('.', ',')+"\n")

            nomeArq = imgArq+'_threshold'+str(i)+'Median.png'
            imgCinza = cv.cvtColor(median, cv.COLOR_BGR2GRAY)
            ret,thresh = cv.threshold(imgCinza,i,255,cv.THRESH_BINARY)
            cv.imwrite(nomeArq,thresh)
            pretos = np.count_nonzero(thresh==0)
            brancos = np.count_nonzero(thresh==255)
            total = pretos+brancos
            percPretos = 100*pretos/total
            percBrancos = 100*brancos/total
            arq.write(nomeArq+"\t"+str(brancos)+"\t"+str(pretos)+"\t"+str(total)+"\t"+str(percBrancos).replace('.', ',')+"\t"+str(percPretos).replace('.', ',')+"\n")

            nomeArq = imgArq+'_threshold'+str(i)+'Bilat.png'
            imgCinza = cv.cvtColor(bilat, cv.COLOR_BGR2GRAY)
            ret,thresh = cv.threshold(imgCinza,i,255,cv.THRESH_BINARY)
            cv.imwrite(nomeArq,thresh)
            pretos = np.count_nonzero(thresh==0)
            brancos = np.count_nonzero(thresh==255)
            total = pretos+brancos
            percPretos = 100*pretos/total
            percBrancos = 100*brancos/total
            arq.write(nomeArq+"\t"+str(brancos)+"\t"+str(pretos)+"\t"+str(total)+"\t"+str(percBrancos).replace('.', ',')+"\t"+str(percPretos).replace('.', ',')+"\n")

arq.close()
