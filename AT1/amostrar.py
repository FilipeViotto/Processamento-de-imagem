import numpy as np
import cv2 as cv

img = cv.imread('newyork.jpg', cv.IMREAD_GRAYSCALE)

imagem_copy = img.copy()
altura = imagem_copy.shape[0] # 1110
largura = imagem_copy.shape[1] # 740
print(f'altura: {altura}\nlargura: {largura}')
possibilidades = [i for i in range(1,altura+1) if altura % i == 0 and largura % i == 0]

cv.imshow('imagem_original',imagem_copy)
cv.waitKey(0)
cv.destroyAllWindows()

def amostrar(imagem_copy,reducao):
    for i in range(0,altura,reducao):
        for j in range(0,largura,reducao):
            soma = 0
            for p_linha in range(i,reducao+i):
                for p_coluna in range(j,reducao+j):
                    soma += imagem_copy[p_linha][p_coluna]
            
            media = soma / (reducao**2)

            for p_linha in range(i,reducao+i):
                for p_coluna in range(j,reducao+j):
                    imagem_copy[p_linha][p_coluna] = media

    cv.imshow(f'imagem_{reducao}',imagem_copy)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    for intervalo in possibilidades:
        amostrar(img.copy(),intervalo)
            