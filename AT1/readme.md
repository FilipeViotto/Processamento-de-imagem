O usuário deve manter a imagem no mesmo diretório dos executáveis.
Pressione 0 (zero) para passar para a próxima imagem.
Não force o fechamento da imagem usando o 'x' superior, senão o programa deve ser finalizado manualmente.

amostrar.py 
Vai fazer a redução espacial de todos os tamanhos possíveis da imagem passada.
Para isso é calculado todos os divisores comuns possíveis para a altura e largura da imagem, 
de modo que os pixeis da amostragem tenham sempre a mesma altura e largura.
O valor da amostra é a média dos pixeis que compuseram a amostra.

quantizar.py
Vai fazer todas as 8 possíveis quantizações da imagem.
A quantidade de niveis da imagem é mostrada no nome da imagem e no terminal.
O código usa divisão inteira para detectar a qual nível cada pixel pertence.