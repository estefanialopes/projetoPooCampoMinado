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

    def setTamanhoFonte(self, tamanho):
        self.__fonte = pygame.font.SysFont("Arial", tamanho)
