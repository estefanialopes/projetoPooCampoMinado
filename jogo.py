
import pygame
import sys
from menu import Menu
from botao import Botao
from tabuleiro import Tabuleiro
class Jogo:
	def __init__(self, altura, largura): #contrutor da classe
		self.__altura = altura
		self.__largura = largura
		self.__run = True

	def getAltura(self):
		return self.__altura
    
	def setAltura(self, altura):
		self.__altura = altura

	def getLargura(self):
		return self.__largura
    
	def setLargura(self, largura):
		self.__largura = largura

	def getRun(self):
		return self.__run
    
	def setRun(self, run):
		self.__run = run

	def inicializaPygame(self):
		#inicializa todos os modulos importados do
		pygame.init()

	def	cria_tela(self):
		pygame.display.init()
		#Cria a superficie de display ou seja cria a tela
		self.tela = pygame.display.set_mode((self.__altura, self.__largura), pygame.SHOWN) #define resolução da tela
		pygame.display.set_caption("Campo Minado")

	def criaTabuleiro(self):
		self.tabuleiro = Tabuleiro(10, 9, 9, self.tela)

	def	carregaFonte(self, tamanho = 96):
		self.fonte_texto = pygame.font.SysFont("Arial", tamanho)# define fonte e tamanho do texto

	def cria_relogio(self):
		self.clock = pygame.time.Clock()

	def roda_jogo(self):
		menu = Menu(self.fonte_texto, self.tela)
		exibe_Jogo = False
		self.carregaImagens()
		self.tabuleiro.criaMatrizTabuleiro()

		while self.__run: #enquanto True o jogo roda 
			for event in pygame.event.get(): #pega os eventos do jogo
				if event.type == pygame.QUIT: #se evento for do tipo quit run recebe false e fecha o jogo
					self.__run = False

			#Preenche a tela com uma for de fundo rgb(40, 40, 60)
			self.tela.fill(pygame.Color(40, 40, 60))
			# se exibe_jogo for false significa que o ususario ainda esta no menu
			if not exibe_Jogo:	
				menu.draw_text("Campo Minado", (255, 128, 128), 430, 100)
				botao_play = Botao(600, 300, self.imgPlay)
				botao_play.desenha(self.tela)
				botao_sair = Botao(600, 440, self.imgSair)
				botao_sair.desenha(self.tela)
				if botao_play.detecta_colisao_mouse():
					if pygame.mouse.get_pressed()[0] == 1:
						exibe_Jogo = True

				if botao_sair.detecta_colisao_mouse():
					if pygame.mouse.get_pressed()[0] == 1:
						self.__run = False
			else: 
				self.tabuleiro.desenhaBordaTabuleiro()
				self.tabuleiro.desenhaTabuleiro()
				#calcula a quantidade de bandeiras a mais em relacao as bombas
				placarBandeiras = self.tabuleiro.getQtdBombas() - self.tabuleiro.getQtdBandeiras()
				menu.setTamanhoFonte(64) 
				#desenha o placar de bandeiras no cabecalho
				menu.draw_text(str(placarBandeiras),(255, 0, 0), 462, 50)
				menu.setTamanhoFonte()

				if self.tabuleiro.getPerdeu():
					self.tabuleiro.mostraTodasBombas()
					#carrega uma fonte menor pro menu
					menu.setTamanhoFonte(32)
					menu.exibeMenuFimJogo('Você perdeu!')
					self.exibeBotoesJogarNovamente()
				elif self.tabuleiro.getVitoria():
					menu.setTamanhoFonte(32)
					menu.exibeMenuFimJogo('Parabéns! Você Venceu!', (20, 240, 60))
					self.exibeBotoesJogarNovamente()
				else:
					self.tabuleiro.detectaClickCelula()
				
			pygame.display.flip()
			self.clock.tick(60) #Limita a velocidade dos frames a 60 vezes por segundo

		pygame.quit() #finaliza pygame 

	def exibeBotoesJogarNovamente(self):
		botaoJogar = Botao(64, 380, self.imgPlayX64)
		botaoSair = Botao(164, 380, self.imgSairX64)
		botaoJogar.desenha(self.tela)
		botaoSair.desenha(self.tela)
		event = pygame.event.wait()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if botaoJogar.detecta_colisao_mouse():
				if event.button == 1:
					self.tela.fill(pygame.Color(40, 40, 60))
					self.resetaJogo()
			if botaoSair.detecta_colisao_mouse():
				if event.button == 1:
					self.__run = False

	def resetaJogo(self):
		self.criaTabuleiro()
		self.tabuleiro.criaMatrizTabuleiro()

	def carregaImagens(self):
		botaoJogar = pygame.image.load('imagens/play.png').convert()
		botaoSair = pygame.image.load('imagens/quit.png').convert()
		self.imgPlayX64 = pygame.transform.scale(botaoJogar, (64, 32))
		self.imgSairX64 = pygame.transform.scale(botaoSair, (64, 32))
		self.imgPlay = pygame.transform.scale(botaoJogar, (128, 64))
		self.imgSair = pygame.transform.scale(botaoSair, (128, 64))