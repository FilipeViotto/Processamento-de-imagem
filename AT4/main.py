import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def linear(imagem, a, b):
    transformed = a * imagem.astype(np.int32) + b
    return np.clip(transformed, 0, 255).astype(np.uint8)

def logaritmica(imagem, c):
    img_float = imagem.astype(np.float32) + 1.0
    log_image = c * np.log10(img_float)
    log_norm = (log_image / log_image.max()) * 255.0
    return np.clip(log_norm, 0, 255).astype(np.uint8)

def exponencial(imagem, c):
    transformada = c * (np.exp(imagem.astype(np.float32))-1)
    return np.clip(transformada, 0, 255).astype(np.uint8)

def gama(imagem, c, gama):
    transformada = c * np.power(imagem.astype(np.float32), gama)
    return np.clip(transformada, 0, 255).astype(np.uint8)

def funcoes(imagem):

    cv.imshow('original', imagem)
    cv.waitKey(0)
    cv.destroyWindow('original')
    
    cv.imshow('linear', linear(imagem, a=1.0, b=5.0))
    cv.waitKey(0)
    cv.destroyWindow('linear')

    cv.imshow('logaritmica', logaritmica(imagem, c=1.0))
    cv.waitKey(0)
    cv.destroyWindow('logaritmica')

    cv.imshow('exponencial', exponencial(imagem, c=1.0))
    cv.waitKey(0)
    cv.destroyWindow('exponencial')

    g = 0.9
    c = 1.0
    cv.imshow(f'FuncaoGama_c={c}_gama={g}', gama(imagem, c=c, gama=g))
    cv.waitKey(0)
    cv.destroyWindow(f'FuncaoGama_c={c}_gama={g}')

def CDF(prob, n):
    cdf = 0
    for i in range(n):
        cdf += prob[i]
    return cdf

def mapear(pixel, prob):
    return 255 * CDF(prob,pixel)

def equalizar(imagem):
    vet = [0 for i in range(256)]
    for i in range(altura):
        for j in range(largura):
            vet[img[i][j]] += 1
    
    prob = [num/float(imagem.shape[0]*imagem.shape[1]) for num in vet]
    imagem_final = imagem.copy()
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            imagem_final[i][j] = mapear(imagem[i][j], prob)
    
    return imagem_final

def funcTransf(vetor):
    t = []
    anterior = 0
    for v in vetor:
        t.append(v+anterior)
        anterior = t[-1]
    
    plt.figure(figsize=(12, 6))
    x = list(range(256))
    plt.bar(x, t, color='blue', width=1.0)
    plt.title("funcao de transformacao")
    plt.xlabel("valores pixeis")
    plt.ylabel("quantidade")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    



img = cv.imread('newyork.jpg', cv.IMREAD_GRAYSCALE)

altura = img.shape[0]
largura = img.shape[1]
print(f'altura: {altura}\nlargura: {largura}')

vetor = [0 for i in range(256)]

for i in range(altura):
    for j in range(largura):
        vetor[img[i][j]] += 1

plt.figure(figsize=(12, 6))
x = list(range(256))
plt.bar(x, vetor, color='blue', width=1.0)
plt.title("Histograma")
plt.xlabel("valores pixeis")
plt.ylabel("quantidade")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#funcoes(img)
funcTransf(vetor)


imagem_equalizada = equalizar(img)

# calcula o histograma da imagem equalizada
vetor = [0 for i in range(256)]
for i in range(altura):
    for j in range(largura):
        vetor[imagem_equalizada[i][j]] += 1
plt.figure(figsize=(12, 6))
x = list(range(256))
plt.bar(x, vetor, color='blue', width=1.0)
plt.title("Histograma equalizado")
plt.xlabel("valores pixeis")
plt.ylabel("quantidade")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

cv.imshow(f'equalizada', imagem_equalizada)
cv.waitKey(0)
cv.destroyWindow(f'equalizada')

