import numpy as np
import cv2 as cv

# Carregar imagens coloridas
imagem1 = cv.imread('img_1.png', cv.IMREAD_COLOR)
imagem2 = cv.imread('img_2.png', cv.IMREAD_COLOR)

# Converter para escala de cinza
imagem1_cinza = cv.cvtColor(imagem1, cv.COLOR_BGR2GRAY)
imagem2_cinza = cv.cvtColor(imagem2, cv.COLOR_BGR2GRAY)

# Calcular diferença e máscara
diferenca = cv.absdiff(imagem1_cinza, imagem2_cinza)
_, mascara = cv.threshold(diferenca, 30, 255, cv.THRESH_BINARY)
# Visualizar a máscara para ver onde as diferenças são detectadas
cv.imshow('Máscara de Diferença (antes do destaque)', mascara)
cv.waitKey(0)
cv.destroyAllWindows()

# Criar a imagem de destaque vermelha (terá as mesmas dimensões da máscara)
destaque = np.zeros_like(cv.cvtColor(mascara, cv.COLOR_GRAY2BGR))
destaque[mascara == 255] = [0, 0, 255]

cv.imshow('Diferenças em Vermelho', destaque)
cv.waitKey(0)
cv.destroyAllWindows()

# Opcional: Sobrepor na imagem original (requer redimensionamento se os tamanhos forem diferentes)
if imagem1.shape[:2] == destaque.shape[:2]:
    imagem1_com_destaque = cv.addWeighted(imagem1, 0.7, destaque.astype(np.uint8), 0.3, 0)
    cv.imshow('Imagem Original com Destaque Vermelho', imagem1_com_destaque.astype(np.uint8))
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("As dimensões da imagem original e do destaque não coincidem para sobreposição direta.")