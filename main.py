import pygame
from jogo import Jogo

jogo = Jogo(1280, 768)

jogo.inicializa_jogo()
jogo.cria_tela()
jogo.criaTabuleiro()
jogo.cria_fonte()
jogo.cria_relogio()
jogo.roda_jogo()

