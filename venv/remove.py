import cv2
import os
import cvzone
from select import select
from sre_constants import SUCCESS
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from numpy import imag

captura = cv2.VideoCapture(0)
captura.set(3,640)
captura.set(4,480)
segmentor = SelfiSegmentation()
fps = cvzone.FPS()

Fundos = os.listdir("Images")
lista_imagens = []
for img in Fundos:
    imagem = cv2.imread(f'Images/{img}')
    lista_imagens.append(imagem)

index = 0
while True:
    SUCCESS, imagem = captura.read()
    img_saida = segmentor.removeBG(imagem,lista_imagens[index],threshold=0.8)
    _,img_saida = fps.update(img_saida)

    cv2.imshow("Image out",img_saida)
    cv2.waitKey(1)

    key = cv2.waitKey(1)
    if key == ord('1'):
        if index >0:
            index-=1
    elif key == ord('2'):
        if index < (len(lista_imagens)-1):
            index+=1
    elif key == ord('0'):
        break

