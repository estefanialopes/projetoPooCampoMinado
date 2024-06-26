import pygame

class Botao():
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.retangulo = self.imagem.get_rect()
        self.retangulo.topleft = (x,y)
    
    
    def desenha(self, screen):
        screen.blit(self.imagem, (self.retangulo.x, self.retangulo.y))
    
    #detecta se o cursor do mouse passou em cima do botão    
    def detecta_colisao_mouse(self):
        posicao = pygame.mouse.get_pos()
        
        return self.retangulo.collidepoint(posicao)
    