import pygame


# inicializar
pygame.init()
tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Brick Breaker Youtube")
tamanho_bola=15
jpgador=100

qtde_linha_bloco = 5
qtde_blocos_linha = 8
qtde_total_bloco =qtde_blocos_linha * qtde_linha_bloco