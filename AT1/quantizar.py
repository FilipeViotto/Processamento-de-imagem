import numpy as np
import cv2 as cv

img = cv.imread('newyork.jpg', cv.IMREAD_GRAYSCALE)

imagem_copy = img.copy()

if __name__ == "__main__":
    altura = imagem_copy.shape[0] # 1110
    largura = imagem_copy.shape[1] # 740
    print(f'{altura} e {largura}')

    for i in range(1,9):
        niveis = 2**i-1
        print(f'quantidade de niveis: {256/(niveis+1)*2}')
        imagem_copy = img.copy()
        for linha in range(altura):
            for coluna in range(largura):
                
                imagem_copy[linha][coluna] = ((imagem_copy[linha][coluna] // niveis)) * niveis
        
        cv.imshow(f'imagem_{int(256/(niveis+1)*2)}_niveis',imagem_copy)
        cv.waitKey(0)
        cv.destroyAllWindows()

