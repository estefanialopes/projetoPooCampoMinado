import pygame
import random
import numpy as np
from celula import Celula
from botao import Botao

class Tabuleiro:
    def __init__(self, qtdBombas,  qtdLinha, qtdColuna, screen):
        self.qtdBombas = qtdBombas
        self.qtdLinha = qtdLinha
        self.qtdColuna = qtdColuna
        self.screen = screen
        self.matrizCelulas = np.zeros((self.qtdLinha, self.qtdColuna), dtype=Celula)
        self.perdeu = False
        self.celulasAbertas = 0
        self.qtdBandeiras = 0
        
    def getVitoria(self):
        return self.celulasAbertas == 71
        
    def criaMatrizTabuleiro(self):
        # Cria uma matriz de zeros
        self.tabuleiro = np.zeros((self.qtdLinha, self.qtdColuna), dtype=int)
        
        # Gera um conjunto de posições únicas aleatórias
        self.bombas = set()
        while len(self.bombas) < self.qtdBombas:
            pos = (random.randint(0, self.qtdLinha - 1), random.randint(0, self.qtdColuna - 1))
            self.bombas.add(pos)
        
        # Define as posições selecionadas como 1
        for pos in self.bombas:
            self.tabuleiro[pos] = 1
        self.inicializaListaImagens()
        posInicial = (360, 130)
        for i in range(len(self.tabuleiro)):
            for j in range(len(self.tabuleiro[i])):
                possuiBomba = self.tabuleiro[i][j] == 1
                celula = Celula(posInicial[0] + i * 64, posInicial[1] + j * 64, possuiBomba, self.listaImagens, (i,j))
                self.matrizCelulas[i][j] = celula; 

    
    def desenhaTabuleiro(self): 
        for linhas in self.matrizCelulas:
            for celula in linhas:
                celula.desenha(self.screen)
    
    def desenhaBordaTabuleiro(self):
        corCinza = (169, 169, 169) 
        border = 20
        rect_width = 576 + 2 * border
        rect_height = 576 + 2 * border
        pygame.draw.rect(self.screen, corCinza, (340, 110, rect_width, rect_height), border)
        pygame.draw.rect(self.screen, corCinza, (340, 50, rect_width, rect_height))
        botao = Botao(392, 60, self.listaImagens["bandeira"])
        botao.desenha(self.screen)
        
    def detectaClickCelula(self):
        for linhas in self.matrizCelulas:
            for celula in linhas:
                if celula.detecta_colisao_mouse():
                    self.checaClicksMouse(celula)
    
    def checaClicksMouse(self, celula):
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 3:
                celula.setBandeiraMarcada(not celula.getBandeiraMarcada())
                if not celula.getBandeiraMarcada(): 
                    self.qtdBandeiras -= 1
                else:
                    self.qtdBandeiras += 1 
            elif event.button == 1 and not celula.getBandeiraMarcada():
                if celula.getPossuiBomba(): 
                    self.perdeu = True
                    celula.setCelulaAberta(True)
                else: 
                    self.validaVizinhos(celula)

    def validaVizinhos(self, celula): 
        vizinhosComBomba = 0
        x = celula.getPosCelula()[0]
        y = celula.getPosCelula()[1]
        vizinhosSemBomba = []
        if x - 1 >= 0:
            if self.matrizCelulas[x - 1][y].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.matrizCelulas[x - 1][y].getCelulaAberta():
                    vizinhosSemBomba.append(self.matrizCelulas[x - 1][y])
        if x - 1 >= 0 and y - 1 >= 0:
            if self.matrizCelulas[x - 1][y - 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.matrizCelulas[x - 1][y - 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.matrizCelulas[x - 1][y - 1])
        if x - 1 >= 0 and y + 1 <= 8: 
            if self.matrizCelulas[x - 1][y + 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.matrizCelulas[x - 1][y + 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.matrizCelulas[x - 1][y + 1])
        if y - 1 >= 0: 
            if self.matrizCelulas[x][y - 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.matrizCelulas[x][y - 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.matrizCelulas[x][y - 1])
        if y + 1 <= 8: 
            if self.matrizCelulas[x][y + 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.matrizCelulas[x][y + 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.matrizCelulas[x][y + 1])
        if x + 1 <= 8 and y - 1 >= 0: 
            if self.matrizCelulas[x + 1][y - 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.matrizCelulas[x + 1][y - 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.matrizCelulas[x + 1][y - 1])
        if x + 1 <= 8: 
            if self.matrizCelulas[x + 1][y].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.matrizCelulas[x + 1][y].getCelulaAberta():
                    vizinhosSemBomba.append(self.matrizCelulas[x + 1][y])
        if x + 1 <= 8 and y + 1 <= 8: 
            if self.matrizCelulas[x + 1][y + 1].getPossuiBomba():
                vizinhosComBomba += 1
            else:
                if not self.matrizCelulas[x + 1][y + 1].getCelulaAberta():
                    vizinhosSemBomba.append(self.matrizCelulas[x + 1][y + 1])

        celula.setQtdBombasVizinhas(vizinhosComBomba)
        if not celula.getCelulaAberta():
            celula.setCelulaAberta(True)
            self.celulasAbertas += 1
        
        if vizinhosComBomba == 0:
            for vizinho in vizinhosSemBomba:
                self.validaVizinhos(vizinho)
        else:
            return

    def mostraTodasBombas(self):
        for pos in self.bombas:
            self.matrizCelulas[pos].setExibeBombasOcultas(True) 
    
    def carregaImagem(self, caminhoImagem):
        imagem = pygame.image.load(caminhoImagem).convert()      
        return pygame.transform.scale(imagem, (64, 64))
    
    def inicializaListaImagens(self): 
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