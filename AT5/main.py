import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def convolucionar(imagem, kernel, mascara, tipo, borda = False, valor_borda = 0):
    altura = imagem.shape[0]
    largura = imagem.shape[1]
    if kernel> altura or kernel > largura:
        print("Kernel is very large.")
        return
    
    imagem_copy = np.zeros(kernel+2, kernel+2)


    altura_copy = imagem_copy.shape[0]
    largura_copy = imagem_copy.shape[1]

    # inserir imagem
    for i in range(altura):
        for j in range(largura):
            imagem_copy[i+1][j+1] = imagem[i][j]

    cv.imshow(f'imagem', imagem)
    cv.imshow(f'equalizada', imagem_copy)
    cv.waitKey(0)
    cv.destroyWindow(f'equalizada')
    return
    
    if tipo == 'media':
        if borda:
            for i in range(1,altura):
                media = 0
                for j in range(1,largura):
                    pass
                    



                


img = cv.imread('newyork.jpg', cv.IMREAD_GRAYSCALE)

altura = img.shape[0]
largura = img.shape[1]
print(f'altura: {altura}\nlargura: {largura}')

convolucionar(img, 3, 1,'media')