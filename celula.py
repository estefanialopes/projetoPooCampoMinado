import pygame
from botao import Botao

class Celula (Botao):
    def __init__(self, x, y, possuiBomba, dicionarioImagens, posCelula):
        super().__init__(x, y, dicionarioImagens["inicial"])
        self.__celulaAberta = False
        self.__possuiBomba = possuiBomba
        self.__bandeiraMarcada = False
        self.__dicionarioImagens = dicionarioImagens
        self.__posCelula = posCelula
        self.__exibeBombasOcultas = False
        self.__qtdBombasVizinhas = 0
        
    def getCelulaAberta(self):
        return self.__celulaAberta
    
    def setCelulaAberta(self, celulaAberta):
        self.__celulaAberta = celulaAberta
        
    def getPossuiBomba(self):
        return self.__possuiBomba
    
    def setPossuiBomba(self, possuiBomba):
        self.__possuiBomba = possuiBomba   
        
    def getBandeiraMarcada(self):
        return self.__bandeiraMarcada
    
    def setBandeiraMarcada(self, bandeiraMarcada):
        self.__bandeiraMarcada = bandeiraMarcada  
    
    def getPosCelula(self):
        return self.__posCelula
    
    def setPosCelula(self, posCelula):
        self.__posCelula= posCelula       
    
    def getExibeBombasOcultas(self):
        return self.__exibeBombasOcultas
    
    def setExibeBombasOcultas(self, exibeBombasOcultas):
        self.__exibeBombasOcultas= exibeBombasOcultas 
    
    def getQtdBombasVizinhas(self):
        return self.__qtdBombasVizinhas
    
    def setQtdBombasVizinhas(self, qtdBombasVizinhas):
        self.__qtdBombasVizinhas= qtdBombasVizinhas 
    
    def desenha(self, screen):
        if not self.__celulaAberta and self.__bandeiraMarcada:
            self._imagem = self.__dicionarioImagens["bandeira"]
        elif self.__possuiBomba and self.__celulaAberta: 
            self._imagem = self.__dicionarioImagens["bombaExplodida"]
        elif self.__possuiBomba and self.__exibeBombasOcultas: 
            self._imagem = self.__dicionarioImagens["bomba"]
        elif not self.__celulaAberta: 
            self._imagem = self.__dicionarioImagens["inicial"]
        elif self.__qtdBombasVizinhas >= 0 and self.__qtdBombasVizinhas <= 8 and not self.__possuiBomba:
            self._imagem = self.__dicionarioImagens[str(self.__qtdBombasVizinhas)]

        if self.__possuiBomba: 
            self._imagem = self.__dicionarioImagens["bomba"]
        screen.blit(self._imagem, (self._retangulo.x, self._retangulo.y)) 
        
    #def desenhaBombaNaocelulaAberta(self, screen):
        #if self.__possuiBomba:
            #self.carregaImagens('imagens/unclicked-bomb.png')
            #screen.blit(self._imagem, (self._retangulo.x, self._retangulo.y))
        
    def carregaImagens(self, caminhoImagem):
        self._imagem = pygame.image.load(caminhoImagem).convert()      
        self._imagem = pygame.transform.scale(self._imagem, (64, 64))

    