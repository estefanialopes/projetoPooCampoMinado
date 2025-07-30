import pygame
from jogo import Jogo

jogo = Jogo(1280, 768)

jogo.inicializaPygame()
jogo.cria_tela()
jogo.criaTabuleiro()
jogo.carregaFonte()
jogo.cria_relogio()
jogo.roda_jogo()

