import pygame

class Botao():
    def __init__(self, x, y, imagem):
        self._imagem = imagem
        self._retangulo = self._imagem.get_rect()
        self._retangulo.topleft = (x,y)
    
    def getImagem(self):
        return self._imagem
    
    def setImagem(self, imagem):
        self._imagem = imagem
    
    def getRetangulo(self):
        return self._retangulo
    
    def setRetangulo(self, retangulo):
        self._retangulo = retangulo
    
    def desenha(self, screen):
        screen.blit(self._imagem, (self._retangulo.x, self._retangulo.y))
    
    #detecta se o cursor do mouse passou em cima do botão    
    def detecta_colisao_mouse(self):
        posicao = pygame.mouse.get_pos()
        
        return self._retangulo.collidepoint(posicao)
    