import pygame
from botao import Botao

class Celula (Botao):
    def __init__(self, x, y, possuiBomba, dicionarioImagens, posCelula):
        super().__init__(x, y, dicionarioImagens["inicial"])
        self.celulaAberta = False
        self.possuiBomba = possuiBomba
        self.bandeiraMarcada = False
        self.dicionarioImagens = dicionarioImagens
        self.posCelula = posCelula
        self.exibeBombasOcultas = False
        self.qtdBombasVizinhas = 0
        
    def desenha(self, screen):
        if not self.celulaAberta and self.bandeiraMarcada:
            self.imagem = self.dicionarioImagens["bandeira"]
        elif self.possuiBomba and self.celulaAberta: 
            self.imagem = self.dicionarioImagens["bombaExplodida"]
        elif self.possuiBomba and self.exibeBombasOcultas: 
            self.imagem = self.dicionarioImagens["bomba"]
        elif not self.celulaAberta: 
            self.imagem = self.dicionarioImagens["inicial"]
        elif self.qtdBombasVizinhas >= 0 and self.qtdBombasVizinhas <= 8 and not self.possuiBomba:
            self.imagem = self.dicionarioImagens[str(self.qtdBombasVizinhas)]

        if self.possuiBomba: 
            self.imagem = self.dicionarioImagens["bomba"]
        screen.blit(self.imagem, (self.retangulo.x, self.retangulo.y)) 
        
    def desenhaBombaNaocelulaAberta(self, screen):
        if self.possuiBomba:
            self.carregaImagens('imagens/unclicked-bomb.png')
            screen.blit(self.imagem, (self.retangulo.x, self.retangulo.y))
        
    def carregaImagens(self, caminhoImagem):
        self.imagem = pygame.image.load(caminhoImagem).convert()      
        self.imagem = pygame.transform.scale(self.imagem, (64, 64))

    