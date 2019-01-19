#Faça um programa em python que abra e reproduza um áudio de um arquivo mp3
import pygame
pygame.init() #inicia a lib
pygame.mixer.music.load('Ex21.mp3') #carrega o arquivo
pygame.mixer.music.play() #da um play na musica
pygame.event.wait() #espera terminar para finalizar a tarefa
