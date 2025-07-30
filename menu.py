import pygame
import sys

class Menu:
    def __init__(self, fonte, tela):
        self.__fonte = fonte
        self.__tela= tela
    
    def getFonte(self):
        return self.__fonte
    
    def setFonte(self, fonte):
        self.__fonte = fonte
        
    def getTela(self):
        return self.__tela
    
    def setTela(self, tela):
        self.__tela = tela

#transforma o texto em imagem e desenha o texto na tela na posição x y
    def draw_text(self, text, color, x, y):
        img = self.__fonte.render(text, True, color)
        self.__tela.blit(img,(x,y))

    def setTamanhoFonte(self, tamanho = 96):
        self.__fonte = pygame.font.SysFont("Arial", tamanho)
        
    def exibeMenuFimJogo(self, textoMenu, color = (255, 0, 0)):
        self.draw_text(textoMenu, color, 20, 300)
        self.draw_text("Jogar Novamente ?", color, 20, 340)
