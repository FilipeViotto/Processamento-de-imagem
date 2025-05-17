import numpy as np
import cv2 as cv
import os


arquivos_baixado = 'imagens_salvas'
os.makedirs(arquivos_baixado, exist_ok=True)

# imagem com cor
imagem1 = cv.imread('img_1.png', cv.IMREAD_COLOR)
imagem2 = cv.imread('img_2.png', cv.IMREAD_COLOR)

altura1 = imagem1.shape[0]
largura1 = imagem1.shape[1]
#print(f'altura: {altura}\nlargura: {largura}')

altura = imagem2.shape[0]
largura = imagem2.shape[1]
#print(f'altura: {altura2}\nlargura: {largura2}')

imagem1_cinza = cv.cvtColor(imagem1, cv.COLOR_BGR2GRAY)
imagem2_cinza = cv.cvtColor(imagem2, cv.COLOR_BGR2GRAY)



#cv.imwrite(os.path.join(arquivos_baixado, 'imagem_original.png'), imagem1_cinza)
cv.imshow(f'imagem original', imagem1_cinza)
cv.waitKey(0)
cv.destroyAllWindows()

#cv.imwrite(os.path.join(arquivos_baixado, 'imagem_modificada.png'), imagem2_cinza)
cv.imshow(f'imagem modificada', imagem2_cinza)
cv.waitKey(0)
cv.destroyAllWindows()


diferenca = cv.absdiff(imagem1_cinza, imagem2_cinza)
#cv.imwrite(os.path.join(arquivos_baixado, 'Diferenca_absoluta.png'), diferenca)
cv.imshow('Diferenca absoluta', diferenca)
cv.waitKey(0)
cv.destroyAllWindows()

limiar = 30
_, mascara = cv.threshold(diferenca, limiar, 255, cv.THRESH_BINARY)
#cv.imwrite(os.path.join(arquivos_baixado, 'Mascara_binaria 70.png'), mascara)
cv.imshow('Mascara binaria', mascara)
cv.waitKey(0)
cv.destroyAllWindows()

destaque = np.zeros_like(cv.cvtColor(mascara, cv.COLOR_GRAY2BGR))
destaque[mascara == 255] = [0, 0, 255]

imagem1_com_destaque = cv.addWeighted(imagem1, 0.7, destaque.astype(np.uint8), 0.3, 0)
#cv.imwrite(os.path.join(arquivos_baixado, 'imagem_com_destaque_vermelho.png'), imagem1_com_destaque.astype(np.uint8))
cv.imshow('Imagem com Destaque Vermelho', imagem1_com_destaque.astype(np.uint8))
cv.waitKey(0)
cv.destroyAllWindows()




# imagem normalizada usa operação aritmética
soma = cv.add(imagem1_cinza, imagem2_cinza)
maior_menor = [imagem1_cinza[0][0]+imagem2_cinza[0][0], imagem1_cinza[0][0]+imagem2_cinza[0][0]]
for i in range(altura1):
    for j in range(largura1):
        if maior_menor[0] < soma[i][j]:
            maior_menor[0] = soma[i][j]
        elif maior_menor[1] > soma[i][j]:
            maior_menor[1] = soma[i][j]

normalizado = np.zeros((altura1, largura1), dtype=np.uint8)
for i in range(altura1):
    for j in range(largura1):
        normalizado[i][j] = 255/(maior_menor[0]-maior_menor[1]) * (soma[i][j]-maior_menor[1])





# os teste com operações logicas foram feitas com imagens com cor.
cv.imwrite(os.path.join(arquivos_baixado, 'imagem_normalizada.png'), normalizado)
cv.imshow('imagem normalizada', normalizado)
cv.waitKey(0)
cv.destroyAllWindows()

usa_and = cv.bitwise_and(imagem1_cinza, imagem2_cinza)
#cv.imwrite(os.path.join(arquivos_baixado, 'usa_and.png'), usa_and)
cv.imshow('usando and', usa_and)
cv.waitKey(0)
cv.destroyAllWindows()

usa_xor = cv.bitwise_xor(imagem1_cinza, imagem2_cinza)
#cv.imwrite(os.path.join(arquivos_baixado, 'usa_xor.png'), usa_xor)
cv.imshow('usando xor', usa_xor)
cv.waitKey(0)
cv.destroyAllWindows()

usa_or = cv.bitwise_or(imagem1_cinza, imagem2_cinza)
#cv.imwrite(os.path.join(arquivos_baixado, 'usa_or.png'), usa_or)
cv.imshow('usando or', usa_or)
cv.waitKey(0)
cv.destroyAllWindows()

usa_not = cv.bitwise_not(imagem2_cinza)
#cv.imwrite(os.path.join(arquivos_baixado, 'usa_not.png'), usa_not)
cv.imshow('usando not', usa_not)
cv.waitKey(0)
cv.destroyAllWindows()



