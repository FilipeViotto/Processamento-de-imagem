import numpy as np
import cv2 as cv

img = cv.imread('moedas.png', cv.IMREAD_GRAYSCALE)
altura = img.shape[0]
largura = img.shape[1]
print(f'altura: {altura}\nlargura: {largura}')

def reduzir_fundo(imagem, fator):
    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] < fator:
                imagem[i][j] = 0
            else:
                imagem[i][j] = 255
    cv.imshow(f'imagem binarizada',imagem)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return imagem

def identificar_objetos1(imagem):
    # Identificar objetos na imagem
    _, imagem_binaria = cv.threshold(imagem, 127, 255, cv.THRESH_BINARY)
    contornos, _ = cv.findContours(imagem_binaria, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Desenhar contornos na imagem original
    imagem_contornada = cv.cvtColor(imagem, cv.COLOR_GRAY2BGR)
    for contorno in contornos:
        cv.drawContours(imagem_contornada, [contorno], -1, (0, 255, 0), 2)

    cv.imshow('Contornos', imagem_contornada)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return contornos

def contar_pixels(imagem):
    cont = 1
    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] == 255:
                if (i<altura-1) and imagem[i+1][j] != 0 and imagem[i+1][j] != 255:
                    imagem[i][j] = imagem[i+1][j]
                elif (j<largura-1) and imagem[i][j+1] != 0 and imagem[i][j+1] != 255:
                    imagem[i][j] = imagem[i][j+1]
                elif i>0 and imagem[i-1][j] != 0 and imagem[i-1][j] != 255:
                    imagem[i][j] = imagem[i-1][j]
                elif j>0 and imagem[i][j-1] != 0 and imagem[i][j-1] != 255:
                    imagem[i][j] = imagem[i][j-1]
                else:
                    imagem[i][j] = cont
                    cont += 1

    return imagem

def destacar_objetos (imagem):
    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] !=0:
                if i>0:
                    if imagem[i-1][j] != 0:
                        if imagem[i-1][j]>imagem[i][j]:
                            imagem[i-1][j] = imagem[i][j]
                        else:
                            imagem[i][j] = imagem[i-1][j]
                        if j>0:
                            if imagem[i-1][j-1] != 0:
                                if imagem[i-1][j-1]>imagem[i][j]:
                                    imagem[i-1][j-1] = imagem[i][j]
                                else:
                                    imagem[i][j] = imagem[i-1][j-1]
                        if j<largura-1:
                            if imagem[i-1][j+1] != 0:
                                if imagem[i-1][j+1]>imagem[i][j]:
                                    imagem[i-1][j+1] = imagem[i][j]
                                else:
                                    imagem[i][j] = imagem[i-1][j+1]
                if i<altura-1:
                    if imagem[i+1][j] != 0:
                        if imagem[i+1][j]>imagem[i][j]:
                            imagem[i+1][j] = imagem[i][j]
                        else:
                            imagem[i][j] = imagem[i+1][j]
                        if j>0:
                            if imagem[i+1][j-1] != 0:
                                if imagem[i+1][j-1]>imagem[i][j]:
                                    imagem[i+1][j-1] = imagem[i][j]
                                else:
                                    imagem[i][j] = imagem[i+1][j-1]
                        if j<largura-1:
                            if imagem[i+1][j+1] != 0:
                                if imagem[i+1][j+1]>imagem[i][j]:
                                    imagem[i+1][j+1] = imagem[i][j]
                                else:
                                    imagem[i][j] = imagem[i+1][j+1]
                if j>0:
                    if imagem[i][j-1] != 0:
                        if imagem[i][j-1]>imagem[i][j]:
                            imagem[i][j-1] = imagem[i][j]
                        else:
                            imagem[i][j] = imagem[i][j-1]
                if j<largura-1:
                    if imagem[i][j+1] != 0:
                        if imagem[i][j+1]>imagem[i][j]:
                            imagem[i][j+1] = imagem[i][j]
                        else:
                            imagem[i][j] = imagem[i][j+1]
    
    for i in range(altura-1,0,-1):
        for j in range(largura-1,0,-1):
            if imagem[i][j] !=0:
                if i>0:
                    if imagem[i-1][j] != 0:
                        if imagem[i-1][j]>imagem[i][j]:
                            imagem[i-1][j] = imagem[i][j]
                        else:
                            imagem[i][j] = imagem[i-1][j]
                        if j>0:
                            if imagem[i-1][j-1] != 0:
                                if imagem[i-1][j-1]>imagem[i][j]:
                                    imagem[i-1][j-1] = imagem[i][j]
                                else:
                                    imagem[i][j] = imagem[i-1][j-1]
                        if j<largura-1:
                            if imagem[i-1][j+1] != 0:
                                if imagem[i-1][j+1]>imagem[i][j]:
                                    imagem[i-1][j+1] = imagem[i][j]
                                else:
                                    imagem[i][j] = imagem[i-1][j+1]
                if i<altura-1:
                    if imagem[i+1][j] != 0:
                        if imagem[i+1][j]>imagem[i][j]:
                            imagem[i+1][j] = imagem[i][j]
                        else:
                            imagem[i][j] = imagem[i+1][j]
                        if j>0:
                            if imagem[i+1][j-1] != 0:
                                if imagem[i+1][j-1]>imagem[i][j]:
                                    imagem[i+1][j-1] = imagem[i][j]
                                else:
                                    imagem[i][j] = imagem[i+1][j-1]
                        if j<largura-1:
                            if imagem[i+1][j+1] != 0:
                                if imagem[i+1][j+1]>imagem[i][j]:
                                    imagem[i+1][j+1] = imagem[i][j]
                                else:
                                    imagem[i][j] = imagem[i+1][j+1]
                if j>0:
                    if imagem[i][j-1] != 0:
                        if imagem[i][j-1]>imagem[i][j]:
                            imagem[i][j-1] = imagem[i][j]
                        else:
                            imagem[i][j] = imagem[i][j-1]
                if j<largura-1:
                    if imagem[i][j+1] != 0:
                        if imagem[i][j+1]>imagem[i][j]:
                            imagem[i][j+1] = imagem[i][j]
                        else:
                            imagem[i][j] = imagem[i][j+1]
    cv.imshow('objetos destacados',imagem)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return imagem

def amostrar(imagem_copy,reducao):
    for i in range(0,altura,reducao):
        for j in range(0,largura,reducao):
            soma = 0
            if (i+reducao) > altura or (j+reducao) > largura:
                continue
            for p_linha in range(i,reducao+i):
                for p_coluna in range(j,reducao+j):
                    soma += imagem_copy[p_linha][p_coluna]
            
            media = soma / (reducao**2)

            for p_linha in range(i,reducao+i):
                for p_coluna in range(j,reducao+j):
                    imagem_copy[p_linha][p_coluna] = media
    return imagem_copy


def contar_objetos(imagem):
    pixel = [0]
    objetos = 0
    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] in pixel:
                continue
            else:
                pixel.append(imagem[i][j])
                objetos += 1
    return objetos

def identificar_objetos(imagem):
    imagem = amostrar(imagem.copy(), 4)
    imagem = reduzir_fundo(imagem, 100)
    imagem = contar_pixels(imagem)
    imagem = destacar_objetos(imagem)
    #imagem = destacar_objetos(imagem)
    objetos = contar_objetos(imagem)
    print(f'Quantidade de objetos: {objetos}')
    



if __name__ == "__main__":
    cv.imshow('original', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    identificar_objetos(img)
