import pygame
import sys

class Menu:
    def __init__(self, fonte, tela):
        self.fonte = fonte
        self.tela= tela
        
#transforma o texto em imagem e desenha o texto na tela na posição x y
    def draw_text(self, text, text_col, x, y):
        img= self.fonte.render(text, True, text_col)
        self.tela.blit(img,(x,y))

    def setTamanhoFonte(self, tamanho):
        self.fonte = pygame.font.SysFont("Arial", tamanho)
