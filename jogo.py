
import pygame
import sys
from menu import Menu
from botao import Botao
from tabuleiro import Tabuleiro
class Jogo:
	def __init__(self, altura, largura): #contrutor da classe
		self.altura = altura
		self.largura = largura
		self.run= True

	def inicializa_jogo(self):
		pygame.init() #inicializa o pygame

	def	cria_tela(self):
		pygame.display.init()
		self.tela = pygame.display.set_mode((self.altura, self.largura), pygame.SHOWN) #define resolução da tela
		pygame.display.set_caption("Campo Minado")

	def criaTabuleiro(self):
		self.tabuleiro = Tabuleiro(10, 9, 9, self.tela)

	def	cria_fonte(self):
		self.fonte_texto = pygame.font.SysFont("Arial", 96)# define fonte e tamanho do texto

	def cria_relogio(self):
		self.clock=pygame.time.Clock()#controla as animações do jogo

	def roda_jogo(self):
		menu = Menu(self.fonte_texto, self.tela)
		exibe_Jogo = False
		self.carrega_imagem()
		self.tabuleiro.criaMatrizTabuleiro()
		while self.run: #enquanto True o jogo roda 
			for event in pygame.event.get(): #pega os eventos do jogo
				if event.type == pygame.QUIT: #se evento for do tipo quit run recebe false e fecha o jogo
					self.run = False

			self.tela.fill(pygame.Color(40, 40, 60))
			if not exibe_Jogo:	
				menu.draw_text("Campo Minado", (255, 128, 128), 430, 100)
				botao_play = Botao(600, 300, self.img_play)
				botao_play.desenha(self.tela)
				botao_sair = Botao(600, 440, self.img_sair)
				botao_sair.desenha(self.tela)
				if botao_play.detecta_colisao_mouse():
					if pygame.mouse.get_pressed()[0] == 1:
						exibe_Jogo = True
						self.tela.fill(pygame.Color(40, 40, 60))

				if botao_sair.detecta_colisao_mouse():
					if pygame.mouse.get_pressed()[0] == 1:
						self.run = False
			elif exibe_Jogo: 
				self.tabuleiro.desenhaBordaTabuleiro()
				self.tabuleiro.desenhaTabuleiro()
				placarBandeiras = self.tabuleiro.getQtdBombas() - self.tabuleiro.getQtdBandeiras()
				menu.setTamanhoFonte(64)
				menu.draw_text(str(placarBandeiras),(255, 0, 0), 462, 50)
				menu.setTamanhoFonte(96)
				if self.tabuleiro.getPerdeu(): 
					self.tabuleiro.mostraTodasBombas()
					menu.draw_text("Voce Perdeu :(", (255, 0, 0), 430, 300)
				if self.tabuleiro.getVitoria():
					self.tela.fill(pygame.Color(40, 40, 60))
					menu.draw_text("Voce Ganhou!!!", (255, 128, 128), 430, 300)

				if not self.tabuleiro.getPerdeu():
					self.tabuleiro.detectaClickCelula()
				
			pygame.display.flip()


			self.clock.tick(60) #redesenha a tela 60 vezes por segundo

		pygame.quit() #finaliza pygame 
	
	def carrega_imagem(self):
		self.img_play = pygame.image.load('imagens/play2.png').convert_alpha()
		self.img_sair = pygame.image.load('imagens/s3.png').convert_alpha()