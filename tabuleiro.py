import pygame
import random
import numpy as np
from celula import Celula
from botao import Botao

class Tabuleiro:
    def __init__(self, qtdBombas,  qtdLinha, qtdColuna, screen):
        self.__qtdBombas = qtdBombas
        self.__qtdLinha = qtdLinha
        self.__qtdColuna = qtdColuna
        self.__screen = screen
        #cria uma matriz do tipo celula, para ser instânciada no futuro
        self.__matrizCelulas = np.zeros((self.__qtdLinha, self.__qtdColuna), dtype=Celula)
        self.__perdeu = False
        self.__celulasAbertas = 0
        self.__qtdBandeiras = 0
        
    def getQtdBombas(self):
        return self.__qtdBombas
    
    def setQtdBombas(self, qtdBombas):
        self.__qtdBombas= qtdBombas 
    
    def getPerdeu(self):
        return self.__perdeu
    
    def setPerdeu(self, perdeu):
        self.__perdeu= perdeu  
    
    def getQtdBandeiras(self):
        return self.__qtdBandeiras
    
    def setQtdBandeiras(self, qtdBandeiras):
        self.__qtdBandeiras= qtdBandeiras    
        
    def getVitoria(self):
        return self.__celulasAbertas == 71
        
    def criaMatrizTabuleiro(self):
        # Cria uma matriz de zeros
        self.tabuleiro = np.zeros((self.__qtdLinha, self.__qtdColuna), dtype=int)
        
        # Gera um conjunto de posições únicas aleatórias para as bombas
        self.bombas = set()
        while len(self.bombas) < self.__qtdBombas:
            pos = (random.randint(0, self.__qtdLinha - 1), random.randint(0, self.__qtdColuna - 1))
            self.bombas.add(pos)
        
        # Define as posições selecionadas como 1
        for pos in self.bombas:
            self.tabuleiro[pos] = 1
        
        self.inicializaListaImagens()
        # verifica se possui bomba, instancia a classe celula e coloca na matriz de celulas
        posInicial = (360, 130)
        for i in range(len(self.tabuleiro)):
            for j in range(len(self.tabuleiro[i])):
                possuiBomba = self.tabuleiro[i][j] == 1
                celula = Celula(posInicial[0] + i * 64, posInicial[1] + j * 64, possuiBomba, self.listaImagens, (i,j))
                self.__matrizCelulas[i][j] = celula; 

    #desenha todas as celulas do tabuleiro
    def desenhaTabuleiro(self): 
        for linhas in self.__matrizCelulas:
            for celula in linhas:
                celula.desenha(self.__screen)
    
    def desenhaBordaTabuleiro(self):
        corCinza = (169, 169, 169) 
        border = 20
        rect_width = 576 + 2 * border
        rect_height = 576 + 2 * border
        pygame.draw.rect(self.__screen, corCinza, (340, 110, rect_width, rect_height), border)
        pygame.draw.rect(self.__screen, corCinza, (340, 50, rect_width, rect_height))
        botao = Botao(392, 60, self.listaImagens["bandeira"])
        botao.desenha(self.__screen)
        
    def detectaClickCelula(self):
        for linhas in self.__matrizCelulas:
            for celula in linhas:
                if celula.detecta_colisao_mouse():
                    self.checaClicksMouse(celula)
    
    def checaClicksMouse(self, celula):
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 3:
                celula.setBandeiraMarcada(not celula.getBandeiraMarcada())
                #calcula a quantidade de bandeiras marcadas para oo contador
                if not celula.getBandeiraMarcada() and not celula.getCelulaAberta(): 
                    self.__qtdBandeiras -= 1
                elif not celula.getCelulaAberta():
                    self.__qtdBandeiras += 1 
                #checa se ao clicar com botão esquerdo do mouse a celula possuir uma bomba perdeu o jogo    
            elif event.button == 1 and not celula.getBandeiraMarcada():
                if celula.getPossuiBomba(): 
                    self.__perdeu = True
                    celula.setCelulaAberta(True)
                else: 
                    self.validaVizinhos(celula)
    #valida se os vizinhos possui bomba e abre as celulas cujo os vizinhos não possuem bomba
    #e para de abrir ao encontar um vizinho que possui bomba
    def validaVizinhos(self, celula): 
        vizinhosComBomba = 0
        x = celula.getPosCelula()[0]
        y = celula.getPosCelula()[1]
        vizinhosSemBomba = []
        if x - 1 >= 0:
            if self.__matrizCelulas[x - 1][y].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.__matrizCelulas[x - 1][y].getCelulaAberta():
                    vizinhosSemBomba.append(self.__matrizCelulas[x - 1][y])
        if x - 1 >= 0 and y - 1 >= 0:
            if self.__matrizCelulas[x - 1][y - 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.__matrizCelulas[x - 1][y - 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.__matrizCelulas[x - 1][y - 1])
        if x - 1 >= 0 and y + 1 <= 8: 
            if self.__matrizCelulas[x - 1][y + 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.__matrizCelulas[x - 1][y + 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.__matrizCelulas[x - 1][y + 1])
        if y - 1 >= 0: 
            if self.__matrizCelulas[x][y - 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.__matrizCelulas[x][y - 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.__matrizCelulas[x][y - 1])
        if y + 1 <= 8: 
            if self.__matrizCelulas[x][y + 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.__matrizCelulas[x][y + 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.__matrizCelulas[x][y + 1])
        if x + 1 <= 8 and y - 1 >= 0: 
            if self.__matrizCelulas[x + 1][y - 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.__matrizCelulas[x + 1][y - 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.__matrizCelulas[x + 1][y - 1])
        if x + 1 <= 8: 
            if self.__matrizCelulas[x + 1][y].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.__matrizCelulas[x + 1][y].getCelulaAberta():
                    vizinhosSemBomba.append(self.__matrizCelulas[x + 1][y])
        if x + 1 <= 8 and y + 1 <= 8: 
            if self.__matrizCelulas[x + 1][y + 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.__matrizCelulas[x + 1][y + 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.__matrizCelulas[x + 1][y + 1])

        celula.setQtdBombasVizinhas(vizinhosComBomba)
        if not celula.getCelulaAberta():
            celula.setCelulaAberta(True)
            self.__celulasAbertas += 1
        
        if vizinhosComBomba == 0:
            for vizinho in vizinhosSemBomba:
                self.validaVizinhos(vizinho)
        else:
            return

    def mostraTodasBombas(self):
        for pos in self.bombas:
            self.__matrizCelulas[pos].setExibeBombasOcultas(True) 
    
    def carregaImagem(self, caminhoImagem):
        imagem = pygame.image.load(caminhoImagem).convert()      
        return pygame.transform.scale(imagem, (64, 64))
    
    def inicializaListaImagens(self): 
        #cria dicionari de imagens e carrega todas imagens 
        self.listaImagens = {
            "inicial": self.carregaImagem('imagens/empty-block.png'),
            "bandeira": self.carregaImagem('imagens/flag.png'),
            "bomba": self.carregaImagem('imagens/unclicked-bomb.png'), 
            "bombaExplodida": self.carregaImagem('imagens/bomb-at-clicked-block.png'),
            "0": self.carregaImagem('imagens/0.png'),
            "1": self.carregaImagem('imagens/1.png'),
            "2": self.carregaImagem('imagens/2.png'),
            "3": self.carregaImagem('imagens/3.png'),
            "4": self.carregaImagem('imagens/4.png'),
            "5": self.carregaImagem('imagens/5.png'),
            "6": self.carregaImagem('imagens/6.png'),
            "7": self.carregaImagem('imagens/7.png'),
            "8": self.carregaImagem('imagens/8.png'),
        }